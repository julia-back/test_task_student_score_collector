from vkbottle.bot import BotLabeler, Message
from vkbottle.dispatch.rules.base import CommandRule


labeler = BotLabeler()


@labeler.private_message(CommandRule("view_scores", prefixes=["!", "/"]))
async def handler_view_score(message: Message):
    pass
