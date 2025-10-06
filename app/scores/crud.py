from http.client import HTTPException

from sqlalchemy.ext.asyncio import AsyncSession
from app.scores.models import Score
from sqlalchemy import select, update
from scores.schemas import CreateScores, UpdateScore


async def get_all_scores(session: AsyncSession) -> list[Score]:
    result = await session.scalars(select(Score))
    return result


async def create_new_score(score_data: CreateScores, session: AsyncSession) -> Score:
    score = Score(**score_data.model_dump())
    session.add(score)
    await session.commit()
    await session.refresh(score)
    return score


async def get_score_by_id(score_id: int, session: AsyncSession) -> Score:
    result = await session.get(Score, score_id)
    if result:
        return result
    else:
        raise HTTPException("Scope not is exist.")


async def update_score_patch(score_id: int, score_data: UpdateScore, session: AsyncSession) -> Score:
    score = await session.get(Score, score_id)
    for key, value in score_data.model_dump().items():
        if hasattr(score, key):
            setattr(score, key, value)
    await session.commit()
    await session.refresh(score)
    return score
