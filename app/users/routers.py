from fastapi import APIRouter, Depends
from users.schemas import CreateUser, ReadUser
from users.crud import create_user_for_register
from sqlalchemy.ext.asyncio import AsyncSession
from database import DatabaseManager


router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/register/", response_model=ReadUser)
async def register_user(user_data: CreateUser, session: AsyncSession = Depends(DatabaseManager.get_session)):
    result = await create_user_for_register(user_data, session)
    return result
