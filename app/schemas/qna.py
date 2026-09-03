from pydantic import BaseModel, Field


class QnaRequest(BaseModel):
    question: str = Field(
        ..., min_length=1, examples=["What is the best selling menu item?"]
    )


class QnaResponse(BaseModel):
    answer: str
