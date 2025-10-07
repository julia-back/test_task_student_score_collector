from pydantic import BaseModel


class UserBase(BaseModel):
    first_name: str
    last_name: str


class CreateUser(UserBase):
    pass


class ReadUser(UserBase):
    id: int
    telegram_id: int | None
    is_active: bool


class UserInDB(UserBase):
    hashed_password: str
