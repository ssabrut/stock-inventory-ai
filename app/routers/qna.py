from fastapi import APIRouter, Depends, HTTPException
from loguru import logger

from app.schemas import QnaRequest, QnaResponse
from app.services.agent import QnaAgent, make_qna_agent

router = APIRouter()


@router.post(
    "/qna",
    response_model=QnaResponse,
    summary="Ask a question about inventory, menu, or transactions",
    tags=["qna"],
)
async def ask_qna(
    payload: QnaRequest,
    agent: QnaAgent = Depends(make_qna_agent),
) -> QnaResponse:
    try:
        answer = agent.ask(payload.question)
    except Exception as e:
        logger.error(f"QnA agent failed: {e}")
        raise HTTPException(status_code=500, detail="Failed to answer question.")

    return QnaResponse(answer=answer)
