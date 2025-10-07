from users.schemas import CreateUser
from sqlalchemy.ext.asyncio import AsyncSession
from users.models import User
from users.services.hash_password import get_hash_user_password


async def create_user_for_register(user_data: CreateUser, session: AsyncSession):
    user_data_dict = user_data.model_dump()

    password = user_data_dict.pop("password")
    user_data_dict["hashed_password"] = get_hash_user_password(password)

    user = User(**user_data_dict)

    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user
