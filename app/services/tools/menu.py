import json
from pathlib import Path

from langchain_core.tools import tool

from app.constant import MENU_FILE


def make_get_menu_tool(data_dir: str):
    @tool
    def get_menu() -> str:
        """Return menu items: id, name, description, price, availability."""
        return json.dumps(json.loads((Path(data_dir) / MENU_FILE).read_text()))

    return get_menu
