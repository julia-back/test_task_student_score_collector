from fastapi import APIRouter
from users.schemas import CreateUser


router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/register/")
def register_user(user: CreateUser):
    pass
