from sqlalchemy.orm import Mapped, mapped_column, validates
from database import Base
from sqlalchemy import String, Integer


class Score(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    subject: Mapped[str] = mapped_column(String(55))
    point: Mapped[int] = mapped_column(Integer)

    @validates("point")
    def validate_point(self, key: str, value: int):
        if value > 100:
            raise ValueError("Point must be <100.")
        elif value < 0:
            raise ValueError("Point must be positive.")
        return value
