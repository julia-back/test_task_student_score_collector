from aiogram import Router, types
from aiogram.filters import Command
from bot_telegram.services.start import sey_hi


router = Router()


@router.message(Command("start"))
async def start_bot(message: types.Message):
    await sey_hi(message)
