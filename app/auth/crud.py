from auth.schemas import AuthUserData, Token
from auth.services import authenticate_user, create_access_token
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession


async def auth_user_and_get_token(user_data: AuthUserData, session: AsyncSession) -> Token:
    user = await authenticate_user(user_data.username, user_data.password, session)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = await create_access_token(data_to_encode={"sub": user.username})

    return Token(access_token=access_token, type_token="bearer")
