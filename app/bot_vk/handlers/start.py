from bot_vk.services.start import say_hi_or_start_register
from vkbottle.bot import BotLabeler, Message
from vkbottle.dispatch.rules.base import CommandRule, StateRule

labeler = BotLabeler()


@labeler.private_message(StateRule(None), text=["Начать", "начать"])
@labeler.private_message(StateRule(None), CommandRule("start", prefixes=["!", "/"]))
async def handler_start(message: Message):
    await say_hi_or_start_register(message)
