from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq()

# Envia uma pergunta ao LLM
response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {
            "role": "system",
            "content": "Você é um assistente especializado em eventos."
        },
        {
            "role": "user",
            "content": "Quero encontrar eventos de tecnologia em Brasília."
        }
    ],
    stream=False
)

print(response.choices[0].message.content)