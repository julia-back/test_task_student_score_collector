from typing import TYPE_CHECKING

from database import Base
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, validates, relationship

if TYPE_CHECKING:
    from users.models import User


class Score(Base):
    __tablename__ = "scores"

    id: Mapped[int] = mapped_column(primary_key=True)
    subject: Mapped[str] = mapped_column(String(55))
    point: Mapped[int] = mapped_column(Integer)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    user_owner: Mapped["User"] = relationship(back_populates="scores")

    @validates("point")
    def validate_point(self, key: str, value: int):
        if value > 100:
            raise ValueError("Point must be <100.")
        elif value < 0:
            raise ValueError("Point must be positive.")
        return value
