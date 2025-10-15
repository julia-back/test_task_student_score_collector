from auth.crud import auth_user_and_get_token
from auth.schemas import AuthUserData, Token
from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from database import DatabaseManager

router = APIRouter(prefix="/token", tags=["Token"])


@router.post("/", response_model=Token)
async def login(user_data: AuthUserData, session: AsyncSession = Depends(DatabaseManager.get_session)):
    result = await auth_user_and_get_token(user_data, session)
    return result
