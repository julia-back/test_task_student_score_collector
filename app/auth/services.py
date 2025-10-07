from users.models import User
from sqlalchemy import select
from fastapi import Depends
from users.services.hash_password import verify_password
from sqlalchemy.ext.asyncio import AsyncSession
from database import DatabaseManager
from datetime import timedelta, datetime
from config import settings
import jwt


async def authenticate_user(username, password, session: AsyncSession = Depends(DatabaseManager.get_session)):
    result = await session.scalars(select(User).where(User.username == username))
    user = result.one_or_none()

    if not user:
        return False

    is_verify_password = verify_password(password, user.hashed_password)
    if not is_verify_password:
        return False

    return user


async def create_access_token(data_to_encode: dict) -> str:
    to_encode = data_to_encode.copy()

    access_token_expire = timedelta(minutes=settings.token.access_token_expire_minutes)
    expire = datetime.now(settings.timezone) + access_token_expire
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, key=settings.token.secret_key, algorithm=settings.token.algorithm)
    return encoded_jwt
