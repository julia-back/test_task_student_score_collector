from fastapi import APIRouter
from scores.schemas import Score


router = APIRouter(prefix="/scores", tags=["Scores"])


@router.get("/", response_model=list[Score])
def get_list_scores():
    pass


@router.post("/new/", response_model=Score)
def create_score():
    pass


@router.get("/{score_id}/", response_model=Score)
def get_score(score_id: int):
    pass


@router.patch("/{score_id}/update/", response_model=Score)
def update_score(score_id: int):
    pass
