from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command, StateFilter
from bot_telegram.services.start import sey_hi_or_start_register
from bot_telegram.services.view_scores import view_user_scores, ask_subject
from bot_telegram.fsm_states import AskSubjectState, RegistrationStates
from aiogram.fsm.context import FSMContext
from bot_telegram.services.register import (ask_username, check_unique_and_save_username,
                                            ask_first_name, save_first_name, ask_last_name,
                                            save_last_name, save_user_data_in_db,
                                            cansel_register)


router = Router()


@router.message(CommandStart())
async def handler_start(message: types.Message):
    await sey_hi_or_start_register(message)


@router.message(F.text == "Начать регистрацию")
@router.message(Command("register"))
async def handler_register(message: types.Message, state: FSMContext):
    await ask_username(message, state)


@router.message(RegistrationStates.wait_for_username)
async def handler_enter_username(message: types.Message, state: FSMContext):
    await check_unique_and_save_username(message, state)
    await ask_first_name(message, state)


@router.message(RegistrationStates.wait_for_first_name)
async def handler_enter_first_name(message: types.Message, state: FSMContext):
    await save_first_name(message, state)
    await ask_last_name(message, state)


@router.message(RegistrationStates.wait_for_last_name)
async def handler_enter_last_name(message: types.Message, state: FSMContext):
    await save_last_name(message,state)
    await save_user_data_in_db(message, state)


@router.message(Command("cansel"), StateFilter(RegistrationStates))
async def handler_cansel_register(message: types.Message, state: FSMContext):
    await cansel_register(message, state)


@router.message(F.text == "Ввести баллы")
@router.message(Command("enter_scores"))
async def handler_enter_scores(message: types.Message): ##############################################################
    pass


@router.message(F.text == "Просмотреть баллы")
@router.message(Command("view_scores"))
async def handler_view_scores(message: types.Message, state: FSMContext):
    await ask_subject(message, state)


@router.message(AskSubjectState.wait_subject)
async def handler_wait_subject(message: types.Message, state: FSMContext):
    await view_user_scores(message, state)
