from pydantic import BaseModel, Field


class Score(BaseModel):

    subject: str = Field(max_length=100)
    point: str = Field(ge=0, le=100)
