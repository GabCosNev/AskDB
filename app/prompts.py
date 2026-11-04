import json

SYSTEM_PROMPT = (
    "Você é um assistente de eventos. "
    "Responda somente com base nos eventos fornecidos. "
    "Não invente eventos, datas ou informações. "
    "Se não houver evento correspondente, informe que não encontrou."
)

def build_user_prompt(events: list[dict], question: str) -> str:
    return (
        f"Eventos disponíveis:\n"
        f"{json.dumps(events, ensure_ascii=False)}\n\n"
        f"Pergunta: {question}"
    )