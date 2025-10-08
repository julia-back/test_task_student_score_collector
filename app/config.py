from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, PostgresDsn
from dotenv import load_dotenv
import os
from datetime import timezone
from typing import Any

load_dotenv()


class RunConfig(BaseModel):
    host: str = "127.0.0.1"
    port: str = 8000


class DatabaseConfig(BaseModel):
    url: PostgresDsn = PostgresDsn(os.getenv("DB__URL"))


class TokenConfig(BaseModel):
    secret_key: str = os.getenv("TOKEN__SECRET_KEY")
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30


class TelegramBotConfig(BaseModel):
    api_key: str = os.getenv("TELEGRAM_BOT__API_KEY")


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_nested_delimiter="__",
        case_sensitive=False
    )

    timezone: Any = timezone.utc

    run: RunConfig = RunConfig()
    db: DatabaseConfig = DatabaseConfig()
    token: TokenConfig = TokenConfig()
    telegram_bot: TelegramBotConfig = TelegramBotConfig()


settings = Settings()
