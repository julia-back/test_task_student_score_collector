from config import settings
from logging_config import app_logger
from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

logger = app_logger.getChild(__name__)


class DatabaseManager:
    def __init__(self, url: str = str(settings.db.url), echo: bool = False):
        self.db_url = url
        self.engine = create_async_engine(url=self.db_url, echo=echo)
        self.session_maker = async_sessionmaker(self.engine, autoflush=False, expire_on_commit=False)

    async def dispose_engine(self):
        await self.engine.dispose()

    @staticmethod
    async def get_session():
        logger.debug("Getting session db.")
        async with db_manager.session_maker() as session:
            yield session


db_manager = DatabaseManager(echo=True)


class Base(AsyncAttrs, DeclarativeBase):
    metadata = MetaData(naming_convention=settings.db.naming_convention)
