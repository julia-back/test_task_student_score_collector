from vkbottle import API
from config import settings
from vkbottle.bot import Bot, BotLabeler
from bot_vk.handlers.start import labeler as start_labeler
from bot_vk.handlers.register import labeler as register_labeler
from bot_vk.handlers.enter_scores import labeler as enter_scores_labeler
from bot_vk.handlers.view_scores import labeler as view_scores_labeler
from middleware import NoBotMiddleware
from bot_vk.states import state_dispenser
import logging


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

api = API(str(settings.vk_bot.api_key))

labeler = BotLabeler()

labeler.message_view.register_middleware(NoBotMiddleware)

labeler.load(start_labeler)
labeler.load(register_labeler)
labeler.load(enter_scores_labeler)
labeler.load(view_scores_labeler)


bot = Bot(api=api,
          labeler=labeler,
          state_dispenser=state_dispenser)


if __name__ == "__main__":
    logger.info("Start vk bot.")
    bot.run_forever()
    logger.info("Stop vk bot.")
