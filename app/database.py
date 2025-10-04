from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from config import settings


class DatabaseManager:
    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(url=url, echo=echo)
        self.session_maker = async_sessionmaker(self.engine, autoflush=False, expire_on_commit=False)

    async def dispose_engine(self):
        await self.engine.dispose()

    async def get_session(self):
        async with self.session_maker() as session:
            yield session


db_manager = DatabaseManager(settings.db.url, echo=True)
