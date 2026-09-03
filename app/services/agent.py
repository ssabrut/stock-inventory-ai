import json
from functools import lru_cache
from pathlib import Path

from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_ollama import ChatOllama

from app.config import Settings, get_settings
from app.constant import INGREDIENTS_FILE, MENU_FILE, SYSTEM_PROMPT, TRANSACTIONS_FILE


class QnaAgent:
    """Wraps a LangChain ReAct agent that answers questions over the
    restaurant's ingredients, menu, and transaction data."""

    def __init__(self, settings: Settings) -> None:
        data_dir = Path(settings.data_dir)

        def _load(filename: str) -> str:
            return json.dumps(json.loads((data_dir / filename).read_text()))

        @tool
        def get_ingredients() -> str:
            """Return current stock inventory: ingredient id, name, amount, unit, purchase date."""
            return _load(INGREDIENTS_FILE)

        @tool
        def get_menu() -> str:
            """Return menu items: id, name, description, price, availability."""
            return _load(MENU_FILE)

        @tool
        def get_transactions() -> str:
            """Return sales transactions: id, timestamp, status, total, line items."""
            return _load(TRANSACTIONS_FILE)

        llm = ChatOllama(model=settings.ollama_model, temperature=0)
        self._agent = create_agent(
            llm,
            [get_ingredients, get_menu, get_transactions],
            system_prompt=SYSTEM_PROMPT,
        )

    def ask(self, question: str) -> str:
        result = self._agent.invoke({"messages": [("human", question)]})
        return result["messages"][-1].content


@lru_cache
def make_qna_agent() -> QnaAgent:
    return QnaAgent(get_settings())
