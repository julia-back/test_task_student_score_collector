from vkbottle.bot import BotLabeler
from vkbottle.bot import Message
from vkbottle.dispatch.rules.base import CommandRule


labeler = BotLabeler()


@labeler.private_message(CommandRule("enter_scores", prefixes=["!", "/"]))
async def handler_enter_scores(message: Message):
    pass
