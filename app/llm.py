import json

from groq import Groq

from app.config import MODEL

client = Groq()

def ask(events: list[dict], question: str) -> str:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "Você é um assistente de eventos. "
                    "Responda somente com base nos eventos fornecidos. "
                    "Não invente eventos, datas ou informações. "
                    "Se não houver evento correspondente, informe que não encontrou."
                ),
            },
            {
                "role": "user",
                "content": (
                    "Eventos disponíveis:\n"
                    f"{json.dumps(events, ensure_ascii=False)}\n\n"
                    f"Pergunta: {question}"
                ),
            },
        ],
        stream=False,
    )
    return response.choices[0].message.content