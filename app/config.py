from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings, loaded from environment variables or .env."""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_version: str = "0.1.0"
    environment: str = "development"
    service_name: str = "stock-inventory-ai"

    ollama_model: str = "qwen3.5:4b"
    data_dir: str = "data"

    langfuse_public_key: str = ""
    langfuse_secret_key: str = ""
    langfuse_host: str = "http://localhost:3000"
    langfuse_qna_prompt_name: str = "qna-system-prompt"


@lru_cache
def get_settings() -> Settings:
    return Settings()
