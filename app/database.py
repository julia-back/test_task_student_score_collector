from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from config import settings
from sqlalchemy.orm import DeclarativeBase


class DatabaseManager:
    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(url=url, echo=echo)
        self.session_maker = async_sessionmaker(self.engine, autoflush=False, expire_on_commit=False)

    async def dispose_engine(self):
        await self.engine.dispose()

    @staticmethod
    async def get_session():
        async with db_manager.session_maker() as session:
            yield session


db_manager = DatabaseManager(str(settings.db.url), echo=True)


class Base(DeclarativeBase):
    pass
