from vkbottle.bot import BotLabeler, Message
from vkbottle.dispatch.rules.base import CommandRule


labeler = BotLabeler()


@labeler.private_message(CommandRule("register", prefixes=["!", "/"]))
async def handler_register(message: Message):
    pass
