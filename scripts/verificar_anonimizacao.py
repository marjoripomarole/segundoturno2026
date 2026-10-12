"""Procura nomes de entrevistados nos arquivos versionados pelo git, antes de publicar.

A lista de nomes NÃO fica no repositório: é um arquivo de texto na pasta privado/ (ignorada
pelo git), com um padrão por linha (expressão regular do Python; linhas com # são comentários).
Cada padrão é buscado como palavra inteira, sem diferenciar maiúsculas. Para liberar um uso
legítimo, use lookahead, por exemplo: Paulo(?! Freire)

Sai com código 1 se encontrar algum nome. Não substitui a leitura humana: nomes que não estão
na lista não são detectados.

Uso: python3 scripts/verificar_anonimizacao.py privado/nomes-a-verificar.txt
"""
import re, subprocess, sys

padroes = [l.strip() for l in open(sys.argv[1], encoding="utf-8") if l.strip() and not l.startswith("#")]
busca = re.compile(r"(?<!\w)(?:" + "|".join(padroes) + r")(?!\w)", re.IGNORECASE)
arquivos = subprocess.run(["git", "ls-files", "-z"], capture_output=True, text=True, check=True).stdout.split("\0")

achados = 0
for f in filter(None, arquivos):
    if f.startswith("privado/"):
        continue
    for n, linha in enumerate(open(f, encoding="utf-8", errors="replace"), 1):
        for m in busca.finditer(linha):
            achados += 1
            print(f"{f}:{n}: {m.group(0)!r} … {linha[max(0, m.start() - 60):m.end() + 60].strip()}")

print(f"{len(padroes)} padrões, {achados} ocorrência(s).")
sys.exit(1 if achados else 0)
