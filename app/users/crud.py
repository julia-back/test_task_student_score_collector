from users.schemas import UserInDB
from sqlalchemy.ext.asyncio import AsyncSession
from users.models import User


async def create_user_for_register(user_data: UserInDB, session: AsyncSession):
    user = User(**user_data.model_dump())
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user
