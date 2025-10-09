from aiogram import Router, types, F
from aiogram.filters import Command, StateFilter
from bot_telegram.fsm_states import RegistrationStates
from aiogram.fsm.context import FSMContext
from bot_telegram.services.register import (ask_username, check_unique_and_save_username,
                                            ask_first_name, save_first_name, ask_last_name,
                                            save_last_name, save_user_data_in_db,
                                            cansel_register)


router = Router()


@router.message(F.text == "Начать регистрацию")
@router.message(Command("register"))
async def handler_register(message: types.Message, state: FSMContext):
    await ask_username(message, state)


@router.message(Command("cansel"), StateFilter(RegistrationStates))
async def handler_cansel_register(message: types.Message, state: FSMContext):
    await cansel_register(message, state)


@router.message(RegistrationStates.wait_for_username)
async def handler_enter_username(message: types.Message, state: FSMContext):
    is_done = await check_unique_and_save_username(message, state)
    if is_done:
        await ask_first_name(message, state)


@router.message(RegistrationStates.wait_for_first_name)
async def handler_enter_first_name(message: types.Message, state: FSMContext):
    is_done = await save_first_name(message, state)
    if is_done:
        await ask_last_name(message, state)


@router.message(RegistrationStates.wait_for_last_name)
async def handler_enter_last_name(message: types.Message, state: FSMContext):
    is_done = await save_last_name(message, state)
    if is_done:
        await save_user_data_in_db(message, state)
