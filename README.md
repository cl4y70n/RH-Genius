# Chatbot de RH Inteligente

## Visão Geral
Chatbot que responde dúvidas de funcionários sobre políticas, benefícios e procedimentos internos usando IA e busca semântica em Google Sheets.

## Funcionalidades
- FAQ dinâmico
- Busca semântica em planilhas
- Respostas contextualizadas
- Lembretes e notificações (extensível)
- Integração Slack/Teams (mock para testes)

## Tecnologias
- LangChain
- Hugging Face (sentence-transformers)
- ChromaDB
- Python
- Slack/Teams API (mock)
- Docker

## Como Rodar

### Local
```bash
pip install -r requirements.txt
python src/main.py
```

### Docker
```bash
docker-compose build
docker-compose up
```

Digite perguntas no terminal e receba respostas.

## Exemplos de perguntas
- "Quais são os benefícios?"
- "Como solicitar férias?"
- "Qual o horário de trabalho?"

## Extensões Futuras
- Multi-idiomas
- Integração real Slack/Teams
- Dashboard administrativo
- Histórico de perguntas e métricas