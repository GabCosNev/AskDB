from typing import Literal
from pydantic import BaseModel, Field

EventType = Literal["ANNOUNCEMENT", "LECTURE", "CELEBRATION"]

class QuestionRequest(BaseModel):
    question: str = Field(min_length=1, max_length=300)

class AnswerResponse(BaseModel):
    answer: str
    post_ids: list[int]

class QueryIntent(BaseModel):
    event_type: EventType | None = None

class Selection(BaseModel):
    post_ids: list[int]
    message: str