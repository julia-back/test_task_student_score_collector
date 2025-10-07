from fastapi import APIRouter, Depends
from auth.schemas import Token, AuthUserData
from sqlalchemy.ext.asyncio import AsyncSession
from database import DatabaseManager
from auth.crud import auth_user_and_get_token


router = APIRouter(prefix="/token", tags=["Token"])


@router.post("/", response_model=Token)
async def get_token(user_data: AuthUserData, session: AsyncSession = Depends(DatabaseManager.get_session)):
    result = await auth_user_and_get_token(user_data, session)
    return result
