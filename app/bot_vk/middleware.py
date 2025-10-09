from vkbottle import BaseMiddleware
from vkbottle.bot import Message


class NoBotMiddleware(BaseMiddleware[Message]):

    async def pre(self) -> None:
        if self.event.from_id < 0:
            self.stop("I`m sorry, you are a bot.")
