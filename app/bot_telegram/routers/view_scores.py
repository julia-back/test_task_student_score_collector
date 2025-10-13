from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from bot_telegram.fsm_states import ViewScoresState
from bot_telegram.services.view_scores import ask_subject_for_view, view_user_scores

router = Router()


@router.message(F.text == "Просмотреть баллы")
@router.message(Command("view_scores"))
async def handler_view_scores(message: types.Message, state: FSMContext):
    await ask_subject_for_view(message, state)


@router.message(ViewScoresState.wait_subject)
async def handler_wait_subject_for_view(message: types.Message, state: FSMContext):
    await view_user_scores(message, state)
