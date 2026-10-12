# Relato metodológico: eleitores pivotais do 2º turno de 2026 em vídeos de redes sociais

> **Período do trabalho:** 11 e 12 de outubro de 2026.
> **Situação:** estudo exploratório e qualitativo, ainda não é a versão científica.
> **Quem fez o quê:**
> - **Pesquisadora** (conta de Instagram @marjoripomarole): definiu objetivos, grupos, método de expansão e publicação. Enviou os vídeos iniciais e autorizou o acesso à conversa em que um colaborador compartilhou vídeos.
> - **Assistente de IA** (Claude, da Anthropic): fez coleta, transcrição, codificação, checagem de fatos e redação, sob instrução da pesquisadora.
> - **Validação humana:** **nenhuma etapa de codificação foi validada por um segundo codificador humano até agora** (ver Limitações).

---

## 1. Pergunta e objetivo

- **Pedido inicial (11/10, manhã):** analisar, "sem viés político nenhum", vídeos de Instagram sobre o 2º turno da eleição presidencial de 2026 (25/10, Flávio Bolsonaro × Lula).
- **Primeira mudança de escopo:** a partir de uma sugestão de um colaborador do projeto, o objetivo passou a ser entender o eleitor típico de quatro grupos que podem decidir o 2º turno:

| Código | Grupo |
|--------|-------|
| G1 | Direita que não gosta de Bolsonaro (ou que vota nele com reservas) |
| G2 | Indecisos, "nenhum dos dois" e abstenção |
| G3 | Eleitores de Renan Santos (Missão) no 1º turno |
| G4 | Eleitores de Augusto Cury (Avante) no 1º turno |
| REF | Demais eleitores (de Flávio ou de Lula), usados como referência |

- **Pergunta reformulada:** logo no início ficou registrado que entrevistas de rua não permitem medir o "eleitor médio". Os vídeos passam por três filtros: quem filma escolhe, a edição recorta e quem envia seleciona. A pergunta foi reformulada em duas (ver [protocolo, seção 2](protocolo-pesquisa-cientifica.md)):
  - **A, qualitativa:** que argumentos, valores e rejeições aparecem nas falas de cada grupo?
  - **B, sobre o gênero:** como quem publica usa a entrevista de rua (enquadramento, edição, legenda)?

---

## 2. Linha do tempo

| Quando | O que foi feito | Resultado |
|--------|-----------------|-----------|
| 11/10, manhã | A pesquisadora enviou os primeiros links. Foram instaladas as ferramentas (yt-dlp) e definido o roteiro de análise neutra | Conteúdos 1 a 4; arquivo [analise-videos-segundo-turno-2026.md](analise-videos-segundo-turno-2026.md) |
| 11/10 | A pesquisadora enviou o story com a ideia de um colaborador | Grupos G1 a G4 e ficha por entrevistado |
| 11/10 | A pesquisadora perguntou como fazer disso um artigo científico | [protocolo-pesquisa-cientifica.md](protocolo-pesquisa-cientifica.md) |
| 11/10 | A pesquisadora pediu "uma pesquisa para publicar hoje" para pessoas do governo e influenciadores | Nota técnica **"Fiel da Balança"**, com dados do TSE e pesquisas, publicada como página privada |
| 11/10 | Mais links enviados pela pesquisadora | Conteúdos 5 a 25 |
| 11/10 | A pesquisadora pediu para procurar vídeos na conversa com o colaborador | Conteúdos 26 a 54 (29 vídeos ainda não enviados) |
| 11/10 | A pesquisadora pediu a expansão por sementes sugerida pelo colaborador. O Instaloader foi testado e bloqueado. A pesquisadora escolheu a navegação assistida no Chrome | Conteúdos 55 a 91 |
| 12/10 | A pesquisadora pediu este relato | Este documento, mais `dados/` e `scripts/` |

---

## 3. Fontes de dados

### 3.1 Resultados oficiais (TSE)
- **Arquivos:** `votacao_candidato_munzona_2026.zip` e `detalhe_votacao_munzona_2026.zip`, do Portal de Dados Abertos do TSE, baixados em 11/10/2026.
- **Processamento:** soma por UF, região e faixa de tamanho de município (eleitores aptos), com o script [scripts/agregar_resultados_tse.py](scripts/agregar_resultados_tse.py).
- **Conferência:** os totais conferem exatamente com a totalização oficial:
  - Flávio: 56.104.503;
  - Lula: 53.879.538;
  - abstenção: 33.469.244.
- **Resultado salvo:** [dados/primeiro_turno_presidente_por_uf.csv](dados/primeiro_turno_presidente_por_uf.csv).

### 3.2 Pesquisas eleitorais
- **Critério:** só números de outubro de 2026 publicados por veículos com ficha técnica (instituto, campo, amostra, margem).
- **Usadas:**

| Instituto | Campo | Fonte usada |
|-----------|-------|-------------|
| Datafolha | 6 e 7/10 | CNN Brasil |
| PoderData/Aya | 5 a 7/10 | Tribuna de Jundiaí |
| AtlasIntel | 3 a 8/10 | Forbes Brasil |
| Real Time Big Data | 6 e 7/10 | NC News |

- **Descartados:**
  - recortes vindos só de um resumo gerado por IA (site Quenty);
  - números de uma pesquisa de **maio** que aparecia em matéria de outubro (ver seção 7).

### 3.3 Vídeos (corpus)
São 91 conteúdos, em três lotes:

| Lote | Conteúdos | Origem | Como foi obtido |
|------|-----------|--------|-----------------|
| 1 | 1 a 25 | Links enviados pela pesquisadora no chat | Enviados manualmente |
| 2 | 26 a 54 | Vídeos compartilhados por um colaborador em conversa privada de Instagram | Leitura da conversa no Chrome da pesquisadora |
| 3 | 55 a 91 | Expansão por perfis-semente e buscas por palavra-chave | Navegação assistida no Chrome da pesquisadora |

A lista completa está em [dados/corpus.csv](dados/corpus.csv): link, perfil, data, curtidas e comentários na coleta, legenda original, grupo e caminho da transcrição.

---

## 4. Coleta dos vídeos

### 4.1 Lote 1: links da pesquisadora
- Cada link foi baixado com **yt-dlp** (versão 2026.08.19, sem login), junto com os metadados: autor, data, curtidas, comentários e legenda.
- **Posts de imagem** (o conteúdo 3 é o único): o yt-dlp não os baixa. A legenda foi lida na página e a imagem inteira foi vista no navegador embutido do aplicativo.

### 4.2 Lote 2: vídeos compartilhados por um colaborador
- **Acesso:** com autorização explícita da pesquisadora, a conversa foi aberta na extensão **Claude in Chrome**, no Chrome dela, já logado.
- **Como os vídeos foram identificados:**
  - Os vídeos compartilhados em DM não aparecem como links no Instagram, e sim como cartões.
  - O código de cada vídeo (o "shortcode") foi lido das propriedades internas da página, enquanto a conversa era rolada.
  - Com a janela do Chrome escondida, o Instagram não renderiza os cartões. Por isso foi preciso rolar com eventos reais de mouse e coletar a cada passo.
- **Resultado:** 31 vídeos encontrados, dos quais 2 já estavam no lote 1. Os 29 restantes viraram os conteúdos 26 a 54.
- **Sugestão do colaborador:** na conversa, ele sugeriu expandir a coleta com ferramentas automatizadas (Instaloader, Apify) a partir de perfis-semente (ver 4.3).
- **Limite:** a parte mais antiga da conversa **não carregou**. O Instagram parou de paginar e deixou o ícone de carregamento travado. Pode haver mais vídeos lá.
- **Efeito colateral:** abrir a conversa marcou como lidas as mensagens novas do colaborador. Nada foi enviado nem alterado na conversa.
- **Lista dos códigos:** [dados/coleta/conversa_colaborador_shortcodes.txt](dados/coleta/conversa_colaborador_shortcodes.txt).

### 4.3 Lote 3: expansão por sementes ("bola de neve")
- **Ferramentas consideradas:**

| Opção | Resultado ou decisão |
|-------|----------------------|
| Instaloader sem login | **Testado e bloqueado** pelo Instagram (erro 401, "Please wait a few minutes") |
| Instaloader com a sessão da pesquisadora | Descartado: viola os termos do Instagram e arrisca a conta pessoal e verificada |
| Apify | Viável, mas pago e dependente de conta; ficou para a versão científica |
| **Navegação assistida no Chrome, em pequena escala** | **Escolhida pela pesquisadora** |

- **Sementes percorridas:** @willzanelati, @vinimachadofc_, @bragaricardooo, @eduhenricooficial, @reporterdemilhoes, @falamirelacosta.
  - Em cada uma, foi aberta a aba de Reels e rolada a página em ritmo humano, listando os códigos.
  - As sementes foram escolhidas entre os criadores da amostra que entrevistam pessoas dos dois lados.
- **Buscas por palavra-chave:**
  - **Com resultado:** "entrevista eleitor flavio bolsonaro", "eleitor cury", "eleitor renan santos", "eleitor indeciso", "entrevista de rua direita".
  - **Sem resultado:** frases mais longas, como "votei no cury segundo turno".
- **Filtro de data sem baixar nada:**
  - O shortcode do Instagram carrega a data de publicação. Ele é o ID do post em base 64, e os bits altos do ID são o horário de criação.
  - O script [scripts/data_do_shortcode.py](scripts/data_do_shortcode.py) faz a conversão. Foi conferido contra a data do yt-dlp em vários vídeos.
  - Foram mantidos só posts de 01/08/2026 em diante.
- **Funil:**

| Etapa | Quantidade |
|-------|-----------|
| Códigos listados (sementes + buscas, com repetições) | cerca de 330 |
| Novos e de 01/08 em diante | 282 |
| Com metadados obtidos | 196 (186 vídeos; os demais eram fotos ou carrosséis) |
| Selecionados para transcrição | 38 |
| Baixados e transcritos | 37 (1 falhou) |

- **Critério de seleção:**
  - prioridade para legendas com sinais dos grupos G1 a G4 ("Cury", "Renan", "indeciso", "nulo"…);
  - entrevistas de rua em vez de monólogos;
  - **limite de cerca de 8 vídeos por autor**;
  - equilíbrio entre rótulos "esquerda" e "direita" nos criadores que perguntam "esquerda ou direita?".
- **Registros:** listas em [dados/coleta/](dados/coleta/); triagem em [dados/coleta/triagem_metadados.csv](dados/coleta/triagem_metadados.csv).
- **Viés conhecido:** a busca do Instagram é **personalizada pela conta que busca**. Os perfis que fazem campanha e aparecem nela são quase todos do campo de Lula. Isso pode refletir o histórico da conta, e não o ecossistema real.

### 4.4 Tentativa no YouTube
- Uma busca no YouTube por entrevistas de rua sobre o 2º turno trouxe quase só noticiário e comentário.
- Não foi incluída no corpus. A conclusão foi que as entrevistas de rua circulam sobretudo no Instagram e no TikTok.

---

## 5. Processamento de cada vídeo

Feito com [scripts/processar_videos.sh](scripts/processar_videos.sh):

1. **Download** do vídeo e dos metadados (yt-dlp).
2. **Áudio:** extração em mono, 16 kHz (ffmpeg).
3. **Transcrição automática** com **Whisper**, modelo *small*, em português. São 90 transcrições. **Não estão no repositório público**, porque contêm nomes e falas completas de cidadãos comuns; ficam disponíveis para pesquisadores mediante solicitação.
4. **Folha de quadros:** um quadro a cada 6 a 8 segundos, montados numa imagem. Serve para ver o que a edição põe na tela: títulos, legendas, números de urna, manchetes, documentos e rostos.
5. **Leitura das legendas na tela** quando o áudio falhou. Exemplos:
   - "rachadinhas", que o Whisper ouviu como "arrastadas de gênero" (conteúdo 12);
   - "o fim da escala 6x1" (conteúdo 10).

**Os vídeos não foram copiados para o projeto.** Ficaram numa pasta temporária, por direitos autorais e por tamanho (cerca de 2 GB).

---

## 6. Análise e codificação

### 6.1 Roteiro por conteúdo
Aplicado a todos, qualquer que seja o lado:

1. **Identificação:** perfil, data, formato, alcance e legenda. Inclui registrar se quem publica é candidato, político ou campanha.
2. **O que mostra:** descrição, sem adjetivos.
3. **Classificação das afirmações:**
   - fato verificável;
   - opinião;
   - alegação sem prova;
   - e, quando checado: correto, impreciso, incorreto, recortado no tempo.
4. **Técnicas de enquadramento:** "teste do projeto", zombaria, legenda que vai além da fala, inserção de "checagem" na tela, caso extremo apresentado como típico etc.
5. **O que falta:** contexto ausente e a versão mais forte do argumento do outro lado.
6. **Como verificar:** fontes primárias.

### 6.2 Ficha por entrevistado
- **Campos:** grupo, voto no 1º turno, intenção no 2º turno, motivos, rejeições, fonte de informação citada.
- **Regra do grupo:** é definido **pelo que a pessoa declara no vídeo**, nunca pelo que o título ou a legenda sugerem.

### 6.3 Contagens
- **Total:** 91 conteúdos e 98 entrevistados.
- **Fora da contagem de entrevistados:**
  - 3: imagem;
  - 37: áudio ininteligível;
  - 43: sem resposta;
  - 59: monólogo de campanha;
  - 82: enquete-relâmpago;
  - 89: sátira;
  - 91: conteúdo educativo.
- **Vídeos com várias pessoas:** cada pessoa que fala de forma identificável conta como 1 entrevistado.
- **Grupos:**

| Grupo | Nº |
|-------|----|
| G1 | 4 |
| G2 | 10 |
| G3 | 4 |
| G4 | 2 |
| REF Lula/esquerda | 20 |
| REF Flávio/direita | 58 |

### 6.4 Formato
- **Lote 1:** análise detalhada por conteúdo.
- **Lotes 2 e 3:** fichas compactas, por causa do volume. Nos vídeos de menor interesse para os grupos-alvo, uma tabela.
- **Síntese:** a seção "Panorama do conjunto" do arquivo de análise é atualizada a cada lote.

---

## 7. Checagem de fatos

- **Quando checar:** cada afirmação factual relevante, tanto do entrevistado quanto do entrevistador ou da legenda, foi checada por busca na web.
- **Prioridade das fontes:**
  1. registros oficiais (TSE, IBGE/PNAD, STF, Agência Brasil);
  2. veículos com ficha técnica;
  3. demais veículos.
- **Fontes de campanha:** citadas como tal.
- **O que não foi verificado:** ficou registrado como "não verificado aqui" na lista **"Afirmações que mais precisam de checagem externa"**, no fim do arquivo de análise.

**Erros pegos e corrigidos durante o trabalho**

| O que | Como foi pego | Correção |
|-------|---------------|----------|
| Recortes "de outubro" do Datafolha que na verdade eram de uma pesquisa de **maio** (matéria da CartaCapital) | A ficha técnica da página não batia com a data | Excluídos; usados só os recortes confirmados pela CNN |
| Recortes vindos de resumo gerado por IA (site Quenty) | A fonte se declarava escrita com IA | Mantidos só os números confirmados em veículo com ficha técnica |
| "Haddad criou a tabela Fipe" (conteúdo 83), que seria marcado como falso | Checagem antes de classificar | Classificado como **essencialmente correto**: ele coordenou o projeto em 1998, na Fipe |
| "Lula condenado em três instâncias" (conteúdo 19), que a legenda do vídeo "corrigia" | Checagem da cronologia judicial | A entrevistada estava essencialmente correta (1ª instância, TRF-4 e STJ antes da anulação); a correção da legenda era enganosa |
| Generalizações no texto da nota técnica ("menor do que qualquer um dos grupos", "abstenção mais alta onde Flávio ganhou") | Revisão dos números antes de publicar | Frases reescritas para dizer só o que os dados mostram |
| Transcrições erradas do Whisper | Leitura das legendas na tela | Corrigidas na análise |

---

## 8. Nota técnica "Fiel da Balança"

- **Pedido:** uma pesquisa "para publicar hoje" para pessoas do governo e influenciadores.
- **O que foi feito:** uma nota técnica exploratória, não um artigo.
- **Conteúdo:**
  - aritmética do 1º turno;
  - destino dos eleitores dos eliminados (Datafolha e PoderData);
  - distribuição regional e por tamanho de município (TSE);
  - abstenção;
  - pesquisas de 2º turno e recortes;
  - simulador aritmético;
  - seção qualitativa sobre os primeiros quatro vídeos.
- **Regras de neutralidade:**
  - os dados foram apresentados mesmo sendo desfavoráveis ao público-alvo (Flávio à frente);
  - não houve recomendações de campanha;
  - as cores dos candidatos seguem a ordem do 1º turno, não as cores dos partidos;
  - o uso de IA está declarado no rodapé.
- **Publicação:** página privada em https://claude.ai/artifact/RCt5JtEJcCfc4eALovKu5J. Arquivo-fonte: [fiel-da-balanca.html](fiel-da-balanca.html).
- **Pendência:** a seção 7 da nota (entrevistas de rua) reflete só os 4 primeiros vídeos e **está desatualizada** frente aos 91 atuais.

---

## 9. Principais resultados até agora

Detalhes no Panorama do arquivo de análise.

1. **G1** tende a Flávio **como instrumento antipetista**, muitas vezes sem citar Bolsonaro.
2. **G2** se divide entre:
   - rejeitar os dois por desempenho;
   - impotência ("meu voto não muda nada");
   - desconexão;
   - idade (voto facultativo).

   A informação nova não mobiliza esse grupo.
3. **G3** mostra lealdade a Renan e tende a branco, nulo ou abstenção.
4. **G4** está dividido e vota com relutância nos dois sentidos.
5. **Baixa informação, desinformação e discurso violento aparecem nos dois lados** quando os dois lados são entrevistados.
6. **O "teste do projeto" aplicado só a eleitores de Flávio superestima a diferença** entre os eleitorados.
7. **Os vídeos mais vistos são os de falas extremas ou ingênuas**, não os mais informativos.
8. **A amostra está concentrada em quem publica**: cerca de 20 conteúdos vêm de candidatos e de um canal do campo de Lula, e quase nenhum perfil de direita aparece como fonte.

---

## 10. Limitações

- **Não é uma amostra representativa:** há seleção por quem filma, quem edita, quem envia (a pesquisadora e o colaborador) e pela busca personalizada.
- **Um único codificador, e ele é uma IA**, sem validação humana nem cálculo de concordância (alfa de Krippendorff). As classificações de grupo e de enquadramento são julgamentos que precisam de revisão.
- **Transcrição automática** (Whisper *small*) com erros em áudio de rua. As citações usadas na nota ou em publicação precisam ser conferidas no vídeo.
- **Classificação a partir de trechos editados:** a pessoa pode ter dito outra coisa fora do corte.
- **Conversa com o colaborador** lida de forma incompleta (a parte mais antiga não carregou).
- **Recorte da expansão:** foi pequena (6 sementes, 5 buscas, 37 vídeos). Ainda não há perfis de direita como fonte.
- **Datas:** a data de publicação não é a data da gravação. Vídeos de julho e agosto refletem a pré-campanha.
- **Alcance:** curtidas e comentários foram coletados em 11/10 e mudam com o tempo. Alguns perfis ocultam curtidas.

---

## 11. Ética, privacidade e termos de uso

- **Vídeos públicos:** todos eram públicos no momento da coleta.
- **Pessoas comuns:** os entrevistados são cidadãos comuns. **Os nomes que aparecem nos arquivos de trabalho, ditos nos próprios vídeos, devem ser removidos antes de qualquer publicação.** Nas publicações, os entrevistados devem ser descritos sem nome, rosto ou perfil.
- **Mensagens privadas:** a conversa com o colaborador foi lida com autorização da pesquisadora, que é parte da conversa. Só os links de vídeo foram registrados; o conteúdo das mensagens não é reproduzido.
- **Conta pessoal:** o uso da conta da pesquisadora foi limitado a navegação em ritmo humano (cerca de 20 páginas). Não houve curtidas, seguidas, mensagens nem automação de login.
- **Termos do Instagram:** o download com yt-dlp e a leitura automatizada de páginas contrariam os termos de uso do Instagram. Para a versão científica, preferir o acesso oficial para pesquisadores (Meta Content Library) ou declarar o método.
- **Redistribuição:** os vídeos não foram e não devem ser redistribuídos. O projeto guarda só links, metadados e transcrições, para fins de pesquisa.
- **Uso de IA:** a coleta, o processamento e a redação usaram IA (Claude). Isso deve ser declarado em qualquer publicação.

---

## 12. Versão pública e anonimização (12/10/2026)

- **O que foi tirado:** antes de tornar o repositório público, os nomes de cidadãos comuns ditos nos vídeos foram substituídos por códigos (E2, E5, E15b…). O código é o número do conteúdo mais uma letra quando há mais de um entrevistado.
- **O que foi generalizado:** detalhes de saúde e deficiência que não eram necessários à análise.
- **Colaborador:** o nome dele foi retirado e o conteúdo das mensagens privadas não é reproduzido.
- **O que não foi publicado:** as transcrições completas e as legendas de terceiros da triagem.
- **Onde está o original:** a versão com nomes fica num arquivo privado da pesquisadora.
- **Políticos, candidatos e perfis que publicaram os vídeos continuam identificados**, porque são atores públicos.

## 13. Reprodutibilidade: o que está no projeto

| Caminho | Conteúdo |
|---------|----------|
| [analise-videos-segundo-turno-2026.md](analise-videos-segundo-turno-2026.md) | Análise de cada conteúdo, fichas por grupo, achados e panorama |
| [protocolo-pesquisa-cientifica.md](protocolo-pesquisa-cientifica.md) | Desenho para a versão científica (seções 1 a 9) e expansão por sementes (seção 10) |
| [relato-metodologico.md](relato-metodologico.md) | Este relato |
| [fiel-da-balanca.html](fiel-da-balanca.html) | Fonte da nota técnica publicada |
| [dados/corpus.csv](dados/corpus.csv) | Os 91 conteúdos: link, perfil, data, lote, grupo, alcance, legenda, transcrição |
| [dados/coleta/](dados/coleta/) | Códigos por semente e busca, candidatos da expansão, triagem e lista dos vídeos compartilhados pelo colaborador |
| [dados/primeiro_turno_presidente_por_uf.csv](dados/primeiro_turno_presidente_por_uf.csv) | Resultado do 1º turno por UF (TSE) |
| [scripts/processar_videos.sh](scripts/processar_videos.sh) | Download, quadros e transcrição |
| [scripts/data_do_shortcode.py](scripts/data_do_shortcode.py) | Data de publicação a partir do link |
| [scripts/triagem_metadados.py](scripts/triagem_metadados.py) | Triagem dos candidatos da expansão |
| [scripts/agregar_resultados_tse.py](scripts/agregar_resultados_tse.py) | Agregação dos arquivos do TSE |

**Ferramentas usadas:**
- yt-dlp 2026.08.19;
- ffmpeg;
- OpenAI Whisper (modelo *small*, português);
- Python 3;
- Instaloader (apenas teste);
- extensão Claude in Chrome e navegador embutido do aplicativo Claude;
- busca na web para checagens.

---

## 14. Próximos passos sugeridos

1. **Revisão humana:** um segundo codificador revisa os grupos e as classificações de enquadramento de uma subamostra (pelo menos 20%), com concordância medida. De preferência alguém de posição política diferente.
2. **Cobrir a lacuna da direita:** identificar criadores de direita que entrevistam eleitores, por indicação de seguidores ou por busca a partir de outra conta, e aplicar a mesma expansão.
3. **Teste espelhado:** buscar ou produzir entrevistas com a mesma pergunta para eleitores dos dois lados ("defenda seu candidato sem citar o outro"; "cite um projeto dele").
4. **Pré-registrar no OSF** o protocolo antes de ampliar a coleta.
5. **Atualizar a seção qualitativa da nota "Fiel da Balança"** com a amostra de 91 conteúdos, se a nota continuar circulando.
6. **Coletar com cronograma diário** até 25/10 e uma semana depois, porque vídeos são apagados.
