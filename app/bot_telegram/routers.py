from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command
from bot_telegram.services.start import sey_hi_or_start_register
from bot_telegram.services.view_scores import view_user_scores


router = Router()


@router.message(CommandStart())
async def handler_start(message: types.Message):
    await sey_hi_or_start_register(message)


@router.message(F.text == "Начать регистрацию")
@router.message(Command("register"))
async def handler_register(message: types.Message): #################################################################
    pass


@router.message(F.text == "Ввести баллы")
@router.message(Command("enter_scores"))
async def handler_enter_scores(message: types.Message):
    pass


@router.message(F.text == "Просмотреть баллы")
@router.message(Command("view_scores"))
async def handler_view_scores(message: types.Message):
    await view_user_scores(message)
