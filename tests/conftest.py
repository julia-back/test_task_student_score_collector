import os
from dotenv import load_dotenv
import asyncpg
from unittest.mock import patch
from app.logging_config import app_logger
import pytest_asyncio
from base_model import Base
from sqlalchemy.ext.asyncio import create_async_engine
import config

loger = app_logger.getChild(__name__)


load_dotenv()
TEST_DB_URL = os.getenv("TEST_DB_URL")
TEST_DB_NAME = os.getenv("TEST_DB_NAME")


@pytest_asyncio.fixture(autouse=True)
async def created_test_db():
    try:
        conn = await asyncpg.connect(TEST_DB_URL.replace("postgresql+asyncpg",
                                                         "postgresql"))
        await conn.execute(f"DROP DATABASE IF EXISTS {TEST_DB_NAME} WITH (FORCE)")
        await conn.execute(f"CREATE DATABASE {TEST_DB_NAME}")
        await conn.close()

        engine = create_async_engine(f"{TEST_DB_URL}/{TEST_DB_NAME}")
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

        db_url = f"{TEST_DB_URL}/{TEST_DB_NAME}"
        with patch.object(config.settings.db, "url", new=db_url):

            yield

    except Exception as e:
        loger.info(f"Error during db connection in test: {e}")
        raise
    finally:
        conn = await asyncpg.connect(TEST_DB_URL.replace("postgresql+asyncpg",
                                                         "postgresql"))
        await conn.execute(f"DROP DATABASE IF EXISTS {TEST_DB_NAME} WITH (FORCE)")
        await conn.close()
        loger.info("Database connection is closed.")
