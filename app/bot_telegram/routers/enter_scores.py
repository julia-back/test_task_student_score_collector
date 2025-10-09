from aiogram import Router, types, F
from aiogram.filters import Command
from bot_telegram.fsm_states import EnterScoreState
from aiogram.fsm.context import FSMContext
from bot_telegram.services.enter_scores import (ask_subject_for_enter_score, save_subject,
                                                ask_point, save_point, save_score_in_db)


router = Router()


@router.message(F.text == "Ввести баллы")
@router.message(Command("enter_scores"))
async def handler_enter_scores(message: types.Message, state: FSMContext):
    await ask_subject_for_enter_score(message, state)


@router.message(EnterScoreState.wait_subject)
async def handler_wait_subject_for_enter(message: types.Message, state: FSMContext):
    await save_subject(message, state)
    await ask_point(message, state)


@router.message(EnterScoreState.wait_score)
async def handler_wait_score_for_enter(message: types.Message, state: FSMContext):
    await save_point(message, state)
    await save_score_in_db(message, state)
