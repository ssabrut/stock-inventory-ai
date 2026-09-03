from langfuse import Langfuse

from app.config import Settings
from app.constant import SYSTEM_PROMPT


def get_qna_system_prompt(settings: Settings) -> str:
    """Fetch the QnA system prompt from Langfuse prompt management, falling
    back to the local constant if Langfuse is unreachable or not configured."""
    client = Langfuse(
        public_key=settings.langfuse_public_key,
        secret_key=settings.langfuse_secret_key,
        host=settings.langfuse_host,
    )
    prompt = client.get_prompt(
        settings.langfuse_qna_prompt_name,
        label="production",
        fallback=SYSTEM_PROMPT,
    )
    return prompt.get_langchain_prompt()
