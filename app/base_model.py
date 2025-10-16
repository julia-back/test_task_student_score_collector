from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy import MetaData
from config import settings


class Base(AsyncAttrs, DeclarativeBase):

    metadata = MetaData(naming_convention=settings.db.naming_convention)
