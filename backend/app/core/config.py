"""Application settings, loaded from environment variables and `.env`."""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Runtime configuration for the backend."""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "ARBITRA"
    api_v1_prefix: str = "/api/v1"
    cors_origins: list[str] = ["http://localhost:5173", "http://localhost:3000"]
    arbitration_strategy: str = "rule_based"


@lru_cache
def get_settings() -> Settings:
    """Return the cached settings instance."""
    return Settings()
