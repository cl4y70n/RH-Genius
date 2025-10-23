# RH Genius – Chatbot Inteligente de RH

## Visão Geral
O **RH Genius** é um **chatbot inteligente voltado para Recursos Humanos**, capaz de responder dúvidas de funcionários sobre políticas, benefícios, procedimentos internos e FAQs corporativas.  

O sistema utiliza **busca semântica**, **embeddings de linguagem natural** e integração com **Slack ou Teams** para fornecer respostas precisas e contextualizadas, agilizando a comunicação interna e reduzindo o tempo gasto em esclarecimentos manuais.

---

## Funcionalidades Principais
- **FAQ Dinâmico:** Perguntas frequentes armazenadas em planilhas (Google Sheets) ou arquivos CSV/Excel.  
- **Busca Semântica:** Respostas são encontradas via embeddings e similaridade de texto.  
- **Respostas Contextualizadas:** O bot gera respostas completas e claras com base nas informações disponíveis.  
- **Integração com Slack / Teams:** Recebe perguntas diretamente da plataforma corporativa (mock inicial disponível).  
- **Lembretes e Notificações:** Possibilidade de enviar alertas sobre prazos, treinamentos ou atualizações de políticas.  
- **Leve e Escalável:** Inicialmente projetado para datasets pequenos, fácil expansão para grandes bases.

---

## Tecnologias Utilizadas
- **Python 3.11+** – Linguagem principal.  
- **LangChain** – Orquestração do pipeline de perguntas e respostas.  
- **Hugging Face Transformers / Sentence-Transformers** – Geração de embeddings para busca semântica.  
- **ChromaDB** – Banco de vetores local para armazenar embeddings.  
- **Google Sheets API / Pandas** – Armazenamento de FAQs e dados de RH.  
- **Slack API / Microsoft Teams API** – Integração de chat (modo mock para teste).  
- **Docker & Docker Compose** – Facilita o deploy e execução isolada do sistema.

---

## Estrutura do Projeto

```

rh-genius/
├── data/
│   └── sheets/
│       └── faq_mock.csv       # Arquivo mock de FAQs do RH
├── src/
│   ├── main.py                # Entry point do chatbot
│   ├── sheets_loader.py       # Conecta e lê dados do Google Sheets
│   ├── preprocessor.py        # Limpeza e chunking de textos
│   ├── embeddings.py          # Geração de embeddings Hugging Face
│   ├── vectorstore.py         # Armazena embeddings e busca semântica
│   ├── qa_pipeline.py         # Pipeline RAG com LangChain
│   ├── slack_bot.py           # Mock do bot de Slack/Teams
│   └── utils.py               # Funções utilitárias
├── requirements.txt           # Dependências do projeto
├── Dockerfile                 # Dockerfile para container
├── docker-compose.yml         # Orquestração Docker Compose
└── README.md                  # Documentação do projeto

````

---

## Como Rodar

### 1. Rodando Localmente
1. Clone o repositório:
```bash
git clone <URL_DO_REPOSITORIO>
cd rh-genius
````

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Coloque seus documentos / planilhas em `data/sheets/`.

   * Um arquivo CSV mock já está incluído (`faq_mock.csv`).

4. Execute o chatbot:

```bash
python src/main.py
```

5. Digite perguntas diretamente no terminal.

   * Exemplo:

     ```
     Digite sua pergunta: Quais são os benefícios?
     ```

---

### 2. Rodando com Docker

1. Construa a imagem:

```bash
docker-compose build
```

2. Inicie o container:

```bash
docker-compose up
```

3. Digite perguntas no terminal do container para receber respostas.

---

## Exemplos de Perguntas

* "Quais são os benefícios oferecidos pela empresa?"
* "Como faço para solicitar férias?"
* "Qual é o horário de trabalho padrão?"
* "Como atualizar meus dados bancários?"
* "Qual é a política de home office?"

O **RH Genius** encontrará a resposta mais relevante e apresentará de forma clara e objetiva.

---

## Arquitetura do Sistema

```
[Funcionário - Slack/Teams]
           │
           ▼
[RH Genius Bot (Flask/FastAPI)]
           │
           ├─> Recebe pergunta
           │
           ├─> Pipeline LangChain
           │       ├─> Google Sheets Loader
           │       ├─> Pré-processamento / Limpeza
           │       ├─> Geração de embeddings (Hugging Face)
           │       └─> Busca semântica em ChromaDB
           │
           └─> LLM (opcional) → resposta contextual
           │
           ▼
[Bot envia resposta ao funcionário]
```

---

## Boas Práticas

* Organize FAQs em planilhas de forma clara e atualizada.
* Nomeie arquivos com descrições objetivas (ex: `Beneficios.csv`, `Ferias.xlsx`).
* Teste com datasets pequenos inicialmente (5–10 perguntas).
* Faça backup de embeddings antes de remover ou atualizar FAQs.

---

## Possíveis Extensões Futuras

* Integração real com **Slack / Teams** corporativo.
* Suporte a múltiplos idiomas.
* Dashboard administrativo para adicionar FAQs sem alterar o código.
* Histórico de perguntas e métricas de uso.
* Alertas automáticos sobre atualizações de políticas ou treinamentos.
* Escalabilidade para milhares de perguntas usando Pinecone ou ChromaDB remoto.

---

## Contato

* Projeto desenvolvido por: **[CLAYTON RAMOS]**
* Contribuições e sugestões podem ser feitas via **GitHub Issues**.
* Email: **[claytonramos334@gmail.com](claytonramos334@gmail.com)]**

```
