# Soma os votos de presidente do 1º turno de 2026 por UF e município a partir dos arquivos do TSE
# votacao_candidato_munzona_2026_BR.csv e detalhe_votacao_munzona_2026_BR.csv (Portal de Dados Abertos).
# Uso: python3 scripts/agregar_resultados_tse.py PASTA_COM_OS_CSV  (gera agg.json na mesma pasta)

import csv,sys,json,collections
T=sys.argv[1]
cand=collections.defaultdict(lambda: collections.Counter())  # (uf) -> candidate -> votes
mun=collections.defaultdict(lambda: collections.Counter())   # (uf,cdmun,nome) -> cand votes
names={}
with open(f"{T}/votacao_candidato_munzona_2026_BR.csv",encoding="latin1") as f:
    r=csv.DictReader(f,delimiter=";")
    for row in r:
        if row["NR_TURNO"]!="1" or row["DS_CARGO"]!="Presidente": continue
        n=row["NM_URNA_CANDIDATO"]; v=int(row["QT_VOTOS_NOMINAIS_VALIDOS"])
        cand[row["SG_UF"]][n]+=v
        mun[(row["SG_UF"],row["CD_MUNICIPIO"],row["NM_MUNICIPIO"])][n]+=v
det=collections.defaultdict(lambda: collections.Counter())
mdet=collections.defaultdict(lambda: collections.Counter())
with open(f"{T}/detalhe_votacao_munzona_2026_BR.csv",encoding="latin1") as f:
    r=csv.DictReader(f,delimiter=";")
    for row in r:
        if row["NR_TURNO"]!="1" or row["DS_CARGO"]!="Presidente": continue
        for k in ["QT_APTOS","QT_COMPARECIMENTO","QT_ABSTENCOES","QT_VOTOS_BRANCOS","QT_TOTAL_VOTOS_NULOS","QT_TOTAL_VOTOS_VALIDOS"]:
            det[row["SG_UF"]][k]+=int(row[k]); mdet[(row["SG_UF"],row["CD_MUNICIPIO"].lstrip("0"),row["NM_MUNICIPIO"])][k]+=int(row[k])
tot=collections.Counter()
for uf in cand: tot.update(cand[uf])
dt=collections.Counter()
for uf in det: dt.update(det[uf])
print("TOTAL", tot.most_common()); print("DET",dict(dt))
json.dump({"cand":{k:dict(v) for k,v in cand.items()},"det":{k:dict(v) for k,v in det.items()},
  "mun":[[k[0],k[1].lstrip("0"),k[2],dict(v)] for k,v in mun.items()],
  "mdet":[[k[0],k[1],k[2],dict(v)] for k,v in mdet.items()]},open(f"{T}/agg.json","w"))
