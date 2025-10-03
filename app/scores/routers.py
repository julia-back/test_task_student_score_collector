from fastapi import APIRouter


router = APIRouter(prefix="/scores", tags=["Scores"])


@router.get("/")
def get_list_scores():
    pass


@router.post("/new/")
def create_score():
    pass


@router.get("/{score_id}/")
def get_score():
    pass


@router.patch("/{score_id}/update/")
def update_score():
    pass
