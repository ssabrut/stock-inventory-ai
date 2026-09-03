from typing import List

from langchain_core.tools import BaseTool

from app.services.tools.ingredients import make_get_ingredients_tool
from app.services.tools.menu import make_get_menu_tool
from app.services.tools.transactions import make_get_transactions_tool


def make_tools(data_dir: str) -> List[BaseTool]:
    """Build the dataset tools available to the QnA agent, bound to data_dir."""
    return [
        make_get_ingredients_tool(data_dir),
        make_get_menu_tool(data_dir),
        make_get_transactions_tool(data_dir),
    ]
