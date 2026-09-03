import json
from pathlib import Path

from langchain_core.tools import tool

from app.constant import TRANSACTIONS_FILE


def make_get_transactions_tool(data_dir: str):
    @tool
    def get_transactions() -> str:
        """Return sales transactions: id, timestamp, status, total, line items."""
        return json.dumps(json.loads((Path(data_dir) / TRANSACTIONS_FILE).read_text()))

    return get_transactions
