# Triagem dos candidatos da expansão: lê os .info.json baixados pelo yt-dlp (sem baixar vídeos)
# e ordena por sinais dos grupos G1–G4 na legenda. Uso: python3 scripts/triagem_metadados.py PASTA
# PASTA deve conter cands.txt e a subpasta meta/ com os .info.json.

import json,glob,re,sys,collections
S=sys.argv[1]
src={l.split()[0]:l.split()[2] for l in open(S+"/cands.txt") if l.strip()}
rows=[]
kw=re.compile(r"entrevist|rua|eleitor|vot[oa]|flávio|flavio|lula|bolsonaro|cury|renan|caiado|zema|indecis|nulo|segundo turno|2º turno|esquerda|direita",re.I)
grp=re.compile(r"cury|renan|caiado|zema|indecis|nulo|branco|não vou votar|nao vou votar|abstenç|terceira via",re.I)
for f in glob.glob(S+"/meta/*.info.json"):
    d=json.load(open(f))
    desc=(d.get("description") or "").replace("\n"," ")
    dur=d.get("duration") or 0
    ok_vid=bool(d.get("formats")) and (d.get("vcodec") not in (None,"none"))
    score=len(kw.findall(desc))
    g=sorted(set(m.lower() for m in grp.findall(desc)))
    rows.append(dict(id=d["id"],up=d.get("channel") or d.get("uploader_id") or "?",date=d.get("upload_date"),dur=round(dur),likes=d.get("like_count"),score=score,g=g,src=src.get(d["id"],"?"),desc=desc[:160],vid=ok_vid))
rows.sort(key=lambda r:(-len(r["g"]),-r["score"],-(r["likes"] or 0)))
json.dump(rows,open(S+"/triage.json","w"),ensure_ascii=False)
print("total meta:",len(rows),"vídeos:",sum(r["vid"] for r in rows))
print(collections.Counter(r["up"] for r in rows if r["vid"]).most_common(40))
for r in rows:
    if r["vid"] and (r["score"]>=1 or r["src"] in("willzanelati","vinimachadofc_","eduhenricooficial","reporterdemilhoes")):
        print(r["id"],r["up"],r["date"],r["dur"],r["likes"],r["score"],r["g"],"|",r["desc"][:110])
