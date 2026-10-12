# Checklist de anonimização

Revisão de 12/10/2026, feita antes de qualquer publicação. Este arquivo lista o que foi tirado ou trocado e onde, **sem os nomes**. A correspondência nome → código fica num arquivo privado da pesquisadora, fora do git.

**Critério:**

- **Saem:** cidadãos comuns entrevistados ou citados nos vídeos, e o colaborador que compartilhou vídeos em conversa privada.
- **Ficam:** políticos, candidatos, figuras públicas, autores citados e os perfis que publicaram os vídeos, porque são atores públicos.

O código é o número do conteúdo em [dados/corpus.csv](dados/corpus.csv), mais uma letra quando há mais de um entrevistado no mesmo vídeo.

## 1. Entrevistados

| Código | Rótulo público | Conteúdo | Onde o nome aparecia | Como ficou |
|--------|----------------|----------|----------------------|------------|
| E2 | Mulher, 60+, bolsonarista | 2 (e repost no 23) | Análise: ficha REF, conteúdo 2 e conteúdo 23 | ☑ "Mulher, 60+ (E2)", "a entrevistada (E2)" |
| E5 | Mulher, eleitora de Flávio | 5 | Análise: ficha REF e conteúdo 5 | ☑ "Mulher (E5)", "a eleitora (E5)" |
| E8 | Homem, eleitor de Flávio | 8 | Análise: ficha REF e conteúdo 8. Corpus: legenda do perfil (`legenda_original`) | ☑ "Homem (E8)"; na legenda, "[nome]" |
| E14 | Homem, 60+, bolsonarista | 14 | Análise: ficha REF e conteúdo 14 | ☑ "Homem, 60+ (E14)" |
| E15b | Jovem jornalista baiano, eleitor de Lula | 15 | Análise: ficha REF e conteúdo 15 | ☑ "(E15b)" |
| E19 | Educadora física, bolsonarista | 19 | Análise: ficha REF e conteúdo 19. Corpus: legenda do perfil, com nome completo | ☑ "Educadora física (E19)"; na legenda, "[nome da entrevistada]" |
| — | Acompanhante de uma entrevistada | 16 | Análise: fala citada no conteúdo 16 | ☑ "[nome]" |
| — | Eleitor de Flávio (tratado por apelido no vídeo) | 54 | Análise: índice e título do conteúdo 54. Corpus: `tema_resumo` | ☑ "Eleitor de Flávio" |
| E31 | Eleitora de Bolsonaro | 31 | Análise: conteúdo 31 | ☑ "(E31)" |
| E39a | Manifestante de direita | 39 | Análise: conteúdo 39 | ☑ "(E39a)" |
| E42a | Eleitora de Flávio, do Piauí | 42 | Análise: conteúdo 42 | ☑ "(E42a, do Piauí)" |
| E42b | Eleitora de Lula | 42 | Análise: conteúdo 42 | ☑ "(E42b)" |
| E45 | Médico, 47 anos, eleitor de Flávio | 45 | Análise: conteúdo 45 (duas vezes) | ☑ "E45" |
| E84 | Assistente social que trabalha com inclusão | 84 | Análise: tabela da expansão | ☑ "(E84)"; dado de deficiência retirado |
| E85a | Técnica de enfermagem desempregada | 85 | Análise: título e item do conteúdo 85 | ☑ "eleitora desempregada", "E85a" |

**Nomes que só existem nas transcrições** (conteúdos 11, 46 e 50, cinco nomes): nunca entraram nos documentos. ☑ As transcrições não são publicadas.

## 2. Dados sensíveis generalizados

| Conteúdo | O que era | Como ficou |
|----------|-----------|------------|
| 69 | Diagnóstico e histórico de saúde da entrevistada (ficha G2 e conteúdo 69) | ☑ "Pessoa adulta"; "relata experiências pessoais difíceis (saúde e rejeição familiar)" |
| 84 | Deficiência da entrevistada | ☑ Retirada; ficou só a profissão |

## 3. Colaborador e conversa privada

| Onde | O que era | Como ficou |
|------|-----------|------------|
| README, créditos | Nome do colaborador | ☑ "um colaborador do projeto" |
| Relato: quadro de autoria e §§ 1, 2, 3.3, 4.2, 10, 11 e 13 | Nome e perfil do Instagram | ☑ "um colaborador", "o colaborador" |
| Relato §4.2 e protocolo §10 | **Citação literal** de mensagem privada | ☑ Paráfrase: sugeriu expandir a coleta com Instaloader/Apify a partir de perfis-semente |
| Análise: Lote 2 (título, origem, tabela) | Nome e perfil | ☑ "vídeos compartilhados por um colaborador" |
| `dados/corpus.csv`, coluna `lote` (29 linhas) | Valor com o primeiro nome do colaborador | ☑ `2-colaborador` (corrigido nesta revisão) |
| `dados/coleta/` | Nome do arquivo com o nome do colaborador | ☑ `conversa_colaborador_shortcodes.txt` |
| Conteúdo das mensagens | — | ☑ Não reproduzido; só os links dos vídeos foram registrados |

☐ **Pendente:** autorização do colaborador para a paráfrase e para um eventual crédito nominal. Até lá, ele aparece só como "um colaborador".

## 4. O que não foi publicado

- ☑ **As 90 transcrições automáticas.** Em `dados/corpus.csv`, a coluna virou `transcricao_disponivel = sob solicitação`. Para pedir acesso, ver [README](README.md#acesso-às-transcrições).
- ☑ **As legendas de terceiros da triagem** (`dados/coleta/triagem_metadados.csv`, coluna de trecho da legenda).
- ☑ **Os vídeos**, por direitos autorais e por tamanho. Só links.

## 5. Busca final por nomes restantes

Feita em 12/10/2026, sobre os arquivos versionados.

| Checagem | Resultado |
|----------|-----------|
| **Lista de nomes** (24 padrões: os nomes da seção 1, os cinco só das transcrições e o colaborador), com [scripts/verificar_anonimizacao.py](scripts/verificar_anonimizacao.py) | ☑ **0 ocorrências.** Controle positivo: os mesmos padrões encontram os nomes nos originais privados, logo a busca funciona |
| **Palavras com inicial maiúscula** (cerca de 1.180 formas distintas), revistas uma a uma | ☑ As pessoas nomeadas que restam são políticos e candidatos (como Lula, Flávio Bolsonaro, Ronaldo Caiado, Renan Santos, Augusto Cury, Wender Clístenes, Washington Quaquá); figuras públicas; autores citados; e perfis que publicaram os vídeos (como Luciano da Luz, Gustavo Cruz, Mirela Costa, Ivan Vieira, Wilson Zanelati, Vinicius Machado, Ricardo Braga Moreira, Roosevelt Pinheiro) |
| **Perfis @ fora da lista de publicadores** | ☑ São criadores com posts próprios, políticos e créditos dentro de legendas públicas. Nenhum é de entrevistado |
| **Palavras em caixa alta** | ☑ Siglas e trechos de legenda; nenhum nome |
| **Trechos da conversa privada** (termos da mensagem original) | ☑ Nenhum |

**Para repetir depois de qualquer edição:**

```bash
python3 scripts/verificar_anonimizacao.py privado/nomes-a-verificar.txt
```

A lista de nomes fica em `privado/`, fora do git. A busca só pega os nomes da lista. Texto novo (codificações, citações, legendas) exige também uma leitura humana.

## 6. Riscos que continuam

- ☐ **Os links levam aos vídeos, onde aparecem rostos e vozes.** Os vídeos já são públicos, mas quem os assistir vê quem foi entrevistado.
- ☐ **Rótulos descritivos somados ao vídeo** (profissão, idade, cidade) facilitam reconhecer alguém. Foram mantidos só os que a análise usa.
- ☐ **As legendas dos perfis** (`legenda_original` no corpus) são texto público de terceiros. Duas tinham nomes de entrevistados e foram editadas. Legendas novas precisam da mesma checagem.
- ☐ **As classificações ainda não foram revistas por um codificador humano** (ver relato, §10).
