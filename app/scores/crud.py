from http.client import HTTPException

from sqlalchemy.ext.asyncio import AsyncSession
from app.scores.models import Score
from sqlalchemy import select, update
from scores.schemas import CreateScores, UpdateScore
import logging


logger = logging.getLogger(__name__)


async def get_all_scores(session: AsyncSession) -> list[Score]:
    try:
        result = await session.scalars(select(Score))
        return result
    except Exception as e:
        logger.critical(f"Error during request from db: {e}")


async def create_new_score(score_data: CreateScores, session: AsyncSession) -> Score:
    try:
        score = Score(**score_data.model_dump())
        session.add(score)
        await session.commit()
        await session.refresh(score)
        return score
    except Exception as e:
        logger.critical(f"Error during request from db: {e}")


async def get_score_by_id(score_id: int, session: AsyncSession) -> Score:
    result = None
    try:
        result = await session.get(Score, score_id)
    except Exception as e:
        logger.critical(f"Error during request from db: {e}")
    if result:
        return result
    else:
        raise HTTPException("Scope not is exist.")


async def update_score_patch(score_id: int, score_data: UpdateScore, session: AsyncSession) -> Score:
    try:
        score = await session.get(Score, score_id)
        for key, value in score_data.model_dump().items():
            if hasattr(score, key):
                setattr(score, key, value)
        await session.commit()
        await session.refresh(score)
        if score:
            return score
    except Exception as e:
        logger.critical(f"Error during request from db: {e}")
