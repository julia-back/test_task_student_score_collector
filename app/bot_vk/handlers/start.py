from vkbottle.bot import Message, BotLabeler
from vkbottle.dispatch.rules.base import CommandRule, StateRule
from bot_vk.services.start import say_hi_or_start_register


labeler = BotLabeler()


@labeler.private_message(StateRule(None), text=["Начать", "начать"])
@labeler.private_message(StateRule(None), CommandRule("start", prefixes=["!", "/"]))
async def handler_start(message: Message):
    await say_hi_or_start_register(message)
