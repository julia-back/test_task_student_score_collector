from auth.crud import auth_user_and_get_token
from auth.schemas import AuthUserData, Token
from fastapi import APIRouter

router = APIRouter(prefix="/token", tags=["Token"])


@router.post("/", response_model=Token)
async def login(user_data: AuthUserData):
    result = await auth_user_and_get_token(user_data)
    return result
