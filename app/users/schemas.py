from pydantic import BaseModel


class UserBase(BaseModel):
    first_name: str
    last_name: str


class CreateUser(UserBase):
    password: str


class ReadUser(UserBase):
    id: int
    telegram_id: int | None
    is_active: bool
    hashed_password: str


class UserInDB(UserBase):
    hashed_password: str
