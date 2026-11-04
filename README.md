# AskDB

API de consulta inteligente que usa **RAG** e a **Groq API** para responder perguntas em linguagem natural a partir de dados de eventos.

> Ask your database anything.

## Como funciona

1. O usuário envia uma pergunta pelo front-end
2. A API carrega os eventos e filtra os aprovados (`APPROVED`)
3. Os eventos e a pergunta são enviados ao LLM como contexto
4. O modelo responde somente com base nos dados fornecidos
5. A resposta é retornada ao front-end

## Tecnologias

- Python 3.11+
- FastAPI
- Groq API (modelo `openai/gpt-oss-20b`)
- Pydantic
- python-dotenv

## Estrutura do projeto

```
askdb/
├── app/
│   ├── main.py          # API FastAPI e rotas
│   ├── config.py        # configurações e variáveis de ambiente
│   ├── repository.py    # leitura e filtro dos dados
│   ├── llm.py           # cliente Groq e chamada ao modelo
│   └── schemas.py       # modelos de request/response
├── sample_data/
│   └── events.json      # dados de exemplo
├── scripts/
├── .env.example
├── requirements.txt
└── README.md
```

## Instalação

```bash
git clone https://github.com/GabCosNev/askdb.git
cd askdb

python -m venv .venv

# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1
# Linux/macOS
source .venv/bin/activate

pip install -r requirements.txt
```

## Configuração

Copie o arquivo de exemplo e adicione sua chave da Groq ([console.groq.com](https://console.groq.com)):

```bash
cp .env.example .env
```

```env
GROQ_API_KEY=sua_chave_aqui
```

## Executando

```bash
uvicorn app.main:app --reload
```

A documentação interativa fica disponível em `http://127.0.0.1:8000/docs`.

## Exemplo de uso

**Requisição**

```bash
curl -X POST http://127.0.0.1:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "Quais palestras sobre inteligência artificial estão disponíveis?"}'
```

**Resposta**

```json
{
  "answer": "Encontrei as seguintes palestras sobre inteligência artificial: ..."
}
```

## Roadmap

- [x] Consulta com contexto fixo (eventos aprovados)
- [x] API com FastAPI
- [ ] Retriever para buscar apenas os eventos relevantes (busca por palavra-chave)
- [ ] Busca semântica com embeddings
- [ ] Integração com banco de dados real
- [ ] Testes automatizados
- [ ] Front-end de consumo

## Licença

MIT