# import os
# from dotenv import load_dotenv
# import asyncpg
# from alembic import command
# from alembic.config import Config
# from unittest.mock import patch
# from app.database import DatabaseManager
# import logging
# import pytest_asyncio
#
# loger = logging.getLogger(__name__)
#
#
# load_dotenv()
# TEST_DB_URL = os.getenv("TEST_DB_URL")
# TEST_DB_NAME = os.getenv("TEST_DB_NAME")
#
#
# @pytest_asyncio.fixture(scope="session")
# async def created_test_db():
#     try:
#         conn = await asyncpg.connect(TEST_DB_URL)
#         await conn.execute(f"DROP DATABASE IF EXISTS {TEST_DB_NAME} WITH (FORCE)")
#         await conn.execute(f"CREATE DATABASE {TEST_DB_NAME}")
#         await conn.close()
#
#         alembic_cfg = Config("/app/alembic.ini")
#         alembic_cfg.set_main_option("sqlalchemy.url", f"{TEST_DB_URL}/{TEST_DB_NAME}")
#         alembic_cfg.set_main_option("script_location", "/app/alembic")
#         command.upgrade(alembic_cfg, "head")
#
#         url = f"{TEST_DB_URL}/{TEST_DB_NAME}"
#         mock_get_session = DatabaseManager(url=url)
#         with patch("app.database.db_manager.get_session", mock_get_session.get_session()):
#
#             yield
#
#     except Exception as e:
#         loger.info(f"Error during db connection in test: {e}")
#         raise
#     finally:
#         conn = await asyncpg.connect(TEST_DB_URL)
#         await conn.execute(f"DROP DATABASE IF EXISTS {TEST_DB_NAME} WITH (FORCE)")
#         await conn.close()
#         loger.info("Database connection is closed.")
