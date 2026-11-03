# AskDB

API de filtro inteligente que usa RAG e a API do Grok para responder
perguntas em linguagem natural sobre os dados de um banco de dados.

## Como funciona

1. O usuário envia uma pergunta pelo front-end
2. A API busca os dados relevantes no banco
3. O contexto encontrado é enviado ao Grok
4. A resposta é retornada ao front-end

## Tecnologias

- Python
- FastAPI
- Grok API (xAI)
- PostgreSQL