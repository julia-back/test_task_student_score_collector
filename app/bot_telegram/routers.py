from aiogram import Router, types
from aiogram.filters import CommandStart, Command
from bot_telegram.services.start import sey_hi_or_start_register


router = Router()


@router.message(CommandStart())
async def handler_start(message: types.Message):
    await sey_hi_or_start_register(message)


@router.message(Command("register"))
async def handler_register(message: types.Message):
    pass


@router.message(Command("enter_scores"))
async def handler_enter_scores(message: types.Message):
    pass


@router.message(Command("view_scores"))
async def handler_view_scores(message: types.Message):
    pass
