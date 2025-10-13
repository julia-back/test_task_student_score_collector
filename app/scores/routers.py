from fastapi import APIRouter, Depends
from scores.schemas import CreateScores, ReadScores, ScoreBase, UpdateScore
from sqlalchemy.ext.asyncio import AsyncSession

from database import DatabaseManager
from scores.crud import create_new_score, get_all_scores, get_score_by_id, update_score_patch

router = APIRouter(prefix="/scores", tags=["Scores"])


@router.get("/", response_model=list[ReadScores])
async def get_list_scores(session: AsyncSession = Depends(DatabaseManager.get_session)):
    return await get_all_scores(session)


@router.post("/new/", response_model=ReadScores)
async def create_score(score_data: CreateScores, session: AsyncSession = Depends(DatabaseManager.get_session)):
    return await create_new_score(score_data, session)


@router.get("/{score_id}/", response_model=ReadScores)
async def get_score(score_id: int, session: AsyncSession = Depends(DatabaseManager.get_session)):
    return await get_score_by_id(score_id, session)


@router.patch("/{score_id}/update/", response_model=ScoreBase)
async def update_score(
    score_id: int, score_data: UpdateScore, session: AsyncSession = Depends(DatabaseManager.get_session)
):
    return await update_score_patch(score_id, score_data, session)
