from auth.schemas import AuthUserData, Token
from sqlalchemy.ext.asyncio import AsyncSession
from users.models import User
from sqlalchemy import select
from fastapi import HTTPException, status
from users.services.hash_password import verify_password


async def auth_user_and_get_token(user_data: AuthUserData, session: AsyncSession):
    username = user_data.username
    result = await session.scalars(select(User).where(User.username == username))
    user = result.one_or_none()

    if user:
        password = user_data.password
        is_verify_password = verify_password(password, user.hashed_password)

        if is_verify_password:
            return Token(access_token="yes", refresh_token="yes")

        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Password not verified.")

    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not exist.")
