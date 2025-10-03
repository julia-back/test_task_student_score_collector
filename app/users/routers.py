from fastapi import APIRouter
from users.schemas import CreateUser
from users.schemas import User


router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/register/", response_model=User)
def register_user(user: CreateUser):
    pass
