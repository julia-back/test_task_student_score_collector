from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import BigInteger


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, unique=True, index=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    telegram_id: Mapped[str] = mapped_column(BigInteger, unique=True, nullable=True)
    hashed_password: Mapped[str]
    is_active: Mapped[bool] = mapped_column(default=True)
