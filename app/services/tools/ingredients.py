import json
from pathlib import Path

from langchain_core.tools import tool

from app.constant import INGREDIENTS_FILE


def make_get_ingredients_tool(data_dir: str):
    @tool
    def get_ingredients() -> str:
        """Return current stock inventory: ingredient id, name, amount, unit, purchase date."""
        return json.dumps(json.loads((Path(data_dir) / INGREDIENTS_FILE).read_text()))

    return get_ingredients
