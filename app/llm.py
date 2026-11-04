from groq import Groq
from app.config import MODEL
from app.prompts import SYSTEM_PROMPT, build_user_prompt

client = Groq()


def ask(events: list[dict], question: str) -> str:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": build_user_prompt(events, question)},
        ],
        stream=False,
    )
    return response.choices[0].message.content