from vkbottle.bot import Message, BotLabeler
from vkbottle.dispatch.rules.base import CommandRule


labeler = BotLabeler()


@labeler.private_message(CommandRule("start", prefixes=["!", "/"]))
async def handler_start(message: Message):
    await message.answer("Hi")
