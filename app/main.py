from fastapi import FastAPI
from app.repository import get_approved_events
from app.llm import ask
from app.schemas import QuestionRequest, AnswerResponse

app = FastAPI(
    title="AskDB",
    description="API de inteligência artificial utilizando RAG, para identificação no banco de dados",
    version="1.0.0",
)

@app.post("/ask")
def ask_question(body: QuestionRequest) -> AnswerResponse:
    events = get_approved_events()
    return AnswerResponse(answer=ask(events, body.question))