from users.schemas import CreateUser
from sqlalchemy.ext.asyncio import AsyncSession
from users.models import User
from users.services.hash_password import get_hash_user_password
import logging


logger = logging.getLogger(__name__)


async def create_user_for_register(user_data: CreateUser, session: AsyncSession):
    user_data_dict = user_data.model_dump()

    password = user_data_dict.pop("password")
    user_data_dict["hashed_password"] = get_hash_user_password(password)

    user = User(**user_data_dict)

    try:
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user
    except Exception:
        logger.critical("Error during request from db, create user.")
