from pydantic import BaseModel, Field


class ScoreBase(BaseModel):
    subject: str = Field(max_length=100)
    point: int = Field(ge=0, le=100)


class CreateScores(ScoreBase):
    pass


class ReadScores(ScoreBase):
    id: int


class UpdateScore(ScoreBase):
    pass
