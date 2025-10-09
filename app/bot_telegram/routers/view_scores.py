from aiogram import Router, types, F
from aiogram.filters import Command
from bot_telegram.services.view_scores import view_user_scores, ask_subject_for_view
from bot_telegram.fsm_states import ViewScoresState
from aiogram.fsm.context import FSMContext


router = Router()


@router.message(F.text == "Просмотреть баллы")
@router.message(Command("view_scores"))
async def handler_view_scores(message: types.Message, state: FSMContext):
    await ask_subject_for_view(message, state)


@router.message(ViewScoresState.wait_subject)
async def handler_wait_subject_for_view(message: types.Message, state: FSMContext):
    await view_user_scores(message, state)
