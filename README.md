# Segundo turno 2026: eleitores pivotais em vídeos de redes sociais

Estudo exploratório e qualitativo sobre como aparecem, em entrevistas de rua publicadas no Instagram, os grupos de eleitores que podem decidir o 2º turno presidencial de 25/10/2026 (Flávio Bolsonaro × Lula):

| Código | Grupo |
|--------|-------|
| G1 | Direita com reservas a Bolsonaro |
| G2 | Indecisos e abstenção |
| G3 | Eleitores de Renan Santos |
| G4 | Eleitores de Augusto Cury |

O projeto inclui também uma nota técnica com dados oficiais do TSE e pesquisas registradas.

> **Versão pública anonimizada.**
> - Os cidadãos comuns entrevistados nos vídeos aparecem por códigos (E2, E5, E15b…), nunca por nome.
> - As transcrições completas não estão aqui; ficam disponíveis para pesquisadores mediante solicitação.
> - **As classificações ainda não foram revisadas por um codificador humano.** Trate os resultados como exploratórios.
>
> Ver [relato-metodologico.md](relato-metodologico.md), seções 10 a 12.

## Por onde começar

| Arquivo | Para quê |
|---------|----------|
| [relato-metodologico.md](relato-metodologico.md) | O que foi feito, como, com que ferramentas, limites e ética. **Comece por aqui.** |
| [analise-videos-segundo-turno-2026.md](analise-videos-segundo-turno-2026.md) | Análise de cada um dos 98 conteúdos, fichas por grupo e panorama do conjunto |
| [protocolo-pesquisa-cientifica.md](protocolo-pesquisa-cientifica.md) | Desenho para a versão científica e plano de expansão por sementes |
| [fiel-da-balanca.html](fiel-da-balanca.html) | Nota técnica "Fiel da Balança" (TSE, pesquisas e simulador) |
| [dados/corpus.csv](dados/corpus.csv) | Os 98 conteúdos: link, perfil, data, lote, grupo, alcance, legenda |
| [dados/reacoes_contraevidencia.csv](dados/reacoes_contraevidencia.csv) | Os 55 confrontos com informação contrária e a reação de cada entrevistado (RQ3, conteúdos 1 a 91) |
| [dados/coleta/](dados/coleta/) | Listas de coleta: sementes, buscas, triagem e vídeos compartilhados pelo colaborador |
| [dados/primeiro_turno_presidente_por_uf.csv](dados/primeiro_turno_presidente_por_uf.csv) | Resultado do 1º turno por UF (TSE) |
| [scripts/](scripts/) | Download, transcrição, triagem e agregação do TSE |

## Números atuais (13/10/2026)

**98 conteúdos e 102 entrevistados**, por grupo:

| Grupo | Nº |
|-------|----|
| G1 | 4 |
| G2 | 11 |
| G3 | 4 |
| G4 | 2 |
| REF Lula/esquerda | 21 |
| REF Flávio/direita | 60 |

O lote 4 (conteúdos 92 a 98) traz a série de entrevistas de Carlinhos Maia nos Stories, recuperada por reposts.

Não é amostra representativa: os vídeos passaram por seleção de quem filmou, de quem editou e de quem enviou.

## Reproduzir

Requisitos: `yt-dlp`, `ffmpeg`, `openai-whisper` e Python 3.

```bash
scripts/processar_videos.sh /tmp/videos DeKsl-aNeFW DdkDk87vk8q
```

```bash
python3 scripts/data_do_shortcode.py DeKsl-aNeFW
```

Os vídeos não estão no repositório, por direitos autorais e por tamanho. Só links e metadados; as transcrições ficam fora da versão pública.

## Créditos

- **Pesquisa:** Marjori Pomarole.
- **Ideia dos grupos e da expansão por sementes:** um colaborador do projeto.
- **Coleta, processamento, checagens e redação:** assistência de IA (Claude, da Anthropic).
