import logging

from fastapi import FastAPI, HTTPException
from app.repository import search_approved_posts
from app.llm import extract_intent, select_posts, LLMUnavailableError
from app.schemas import QuestionRequest, AnswerResponse

logger = logging.getLogger("askdb")

app = FastAPI(title="AskDB", version="2.0.0")

NOT_FOUND = "Não encontrei eventos que correspondam ao seu pedido."


@app.post("/ask")
def ask_question(body: QuestionRequest) -> AnswerResponse:
    try:
        intent = extract_intent(body.question)
        posts = search_approved_posts(intent.event_type)
        if not posts:
            return AnswerResponse(answer=NOT_FOUND, post_ids=[])

        selection = select_posts(posts, body.question)
    except LLMUnavailableError:
        raise HTTPException(
            status_code=503,
            detail="O assistente está indisponível no momento. Tente novamente em instantes.",
        )
    except Exception:
        logger.exception("Erro inesperado em /ask")
        raise HTTPException(
            status_code=500,
            detail="Não foi possível processar sua pergunta.",
        )

    valid_ids = {p["id"] for p in posts}
    ids = [i for i in selection.post_ids if i in valid_ids]
    if not ids:
        return AnswerResponse(answer=NOT_FOUND, post_ids=[])

    return AnswerResponse(answer=selection.message, post_ids=ids)