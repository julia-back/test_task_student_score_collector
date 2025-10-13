from aiogram import Router, types
from aiogram.filters import CommandStart
from bot_telegram.services.start import sey_hi_or_start_register

router = Router()


@router.message(CommandStart())
async def handler_start(message: types.Message):
    await sey_hi_or_start_register(message)
