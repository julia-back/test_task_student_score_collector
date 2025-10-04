from pydantic_settings import BaseSettings
from pydantic import BaseModel
from dotenv import load_dotenv
import os


load_dotenv()


class RunConfig(BaseModel):
    host: str = "127.0.0.1"
    port: str = 8000


class DatabaseConfig(BaseModel):
    url: str = os.getenv("DATABASE_URL")


class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    db: DatabaseConfig = DatabaseConfig()


settings = Settings()
