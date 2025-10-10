from vkbottle.bot import BotLabeler, Message
from vkbottle.dispatch.rules.base import CommandRule, StateRule
from bot_vk.states import ViewScoresState
from bot_vk.services.view_scores import ask_subject_for_view_scores, view_user_scores


labeler = BotLabeler()


@labeler.private_message(StateRule(None), text="Просмотреть баллы")
@labeler.private_message(StateRule(None),
                         CommandRule("view_scores", prefixes=["!", "/"]))
async def handler_view_score(message: Message):
    await ask_subject_for_view_scores(message)


@labeler.private_message(StateRule(ViewScoresState.wait_subject))
async def handler_enter_subject_for_view_score(message: Message):
    await view_user_scores(message)
