from bot_vk.handlers.enter_scores import labeler as enter_scores_labeler
from bot_vk.handlers.register import labeler as register_labeler
from bot_vk.handlers.start import labeler as start_labeler
from bot_vk.handlers.view_scores import labeler as view_scores_labeler
from bot_vk.states import state_dispenser
from config import settings
from logging_config import app_logger, logging_queue_listener
from bot_vk.middleware import NoBotMiddleware
from vkbottle import API
from vkbottle.bot import Bot, BotLabeler

logger = app_logger.getChild(__name__)

api = API(str(settings.vk_bot.api_key))


labeler = BotLabeler()
labeler.load(start_labeler)
labeler.load(register_labeler)
labeler.load(enter_scores_labeler)
labeler.load(view_scores_labeler)

labeler.message_view.register_middleware(NoBotMiddleware)

bot = Bot(api=api, labeler=labeler, state_dispenser=state_dispenser)


if __name__ == "__main__":
    logging_queue_listener.start()
    logger.critical("Start vk bot.")
    bot.run_forever()
    logger.info("Stop vk bot.")
    logging_queue_listener.stop()
