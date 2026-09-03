from functools import lru_cache

from langchain.agents import create_agent
from langchain_ollama import ChatOllama

from app.config import Settings, get_settings
from app.services.prompts import get_qna_system_prompt
from app.services.tools import make_tools


class QnaAgent:
    """Wraps a LangChain ReAct agent that answers questions over the
    restaurant's ingredients, menu, and transaction data."""

    def __init__(self, settings: Settings) -> None:
        llm = ChatOllama(model=settings.ollama_model, temperature=0)
        self._agent = create_agent(
            llm,
            make_tools(settings.data_dir),
            system_prompt=get_qna_system_prompt(settings),
        )

    def ask(self, question: str) -> str:
        result = self._agent.invoke({"messages": [("human", question)]})
        return result["messages"][-1].content


@lru_cache
def make_qna_agent() -> QnaAgent:
    return QnaAgent(get_settings())
