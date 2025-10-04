from fastapi import APIRouter
from scores.schemas import Score


router = APIRouter(prefix="/scores", tags=["Scores"])


@router.get("/", response_model=list[Score])
async def get_list_scores():
    pass


@router.post("/new/", response_model=Score)
async def create_score():
    pass


@router.get("/{score_id}/", response_model=Score)
async def get_score(score_id: int):
    pass


@router.patch("/{score_id}/update/", response_model=Score)
async def update_score(score_id: int):
    pass
