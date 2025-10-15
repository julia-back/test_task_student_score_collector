from bot_vk.services.enter_scores import (ask_subject_for_enter_scores, cansel_enter_score,
                                          save_subject_ask_point_for_enter_score, save_user_score_in_db)
from bot_vk.states import EnterScoresState
from vkbottle.bot import BotLabeler, Message
from vkbottle.dispatch.rules.base import CommandRule, StateGroupRule, StateRule

labeler = BotLabeler()


@labeler.private_message(StateRule(None), text="Ввести баллы")
@labeler.private_message(StateRule(None), CommandRule("enter_scores", prefixes=["!", "/"]))
async def handler_enter_scores(message: Message):
    await ask_subject_for_enter_scores(message)


@labeler.private_message(CommandRule("cansel", prefixes=["!", "/"]), StateGroupRule(EnterScoresState))
async def handler_cansel_enter_score(message: Message):
    await cansel_enter_score(message)


@labeler.private_message(StateRule(EnterScoresState.wait_subject))
async def handler_enter_subject_for_enter_score(message: Message):
    await save_subject_ask_point_for_enter_score(message)


@labeler.private_message(StateRule(EnterScoresState.wait_point))
async def handler_enter_point_for_enter_score(message: Message):
    await save_user_score_in_db(message)
