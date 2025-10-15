from bot_vk.services.register import (cansel_register, save_first_name_ask_last_name, save_user_data_in_db,
                                      save_username_ask_first_name, start_register_ask_username)
from bot_vk.states import RegisterState
from vkbottle.bot import BotLabeler, Message
from vkbottle.dispatch.rules.base import CommandRule, StateGroupRule, StateRule

labeler = BotLabeler()


@labeler.private_message(StateRule(None), text="Начать регистрацию")
@labeler.private_message(StateRule(None), CommandRule("register", prefixes=["!", "/"]))
async def handler_register(message: Message):
    await start_register_ask_username(message)


@labeler.private_message(CommandRule("cansel", prefixes=["!", "/"]), StateGroupRule(RegisterState))
async def handler_cansel_register(message: Message):
    await cansel_register(message)


@labeler.private_message(StateRule(RegisterState.wait_username_state))
async def handler_enter_username(message: Message):
    await save_username_ask_first_name(message)


@labeler.private_message(StateRule(RegisterState.wait_first_name_state))
async def handler_enter_first_name(message: Message):
    await save_first_name_ask_last_name(message)


@labeler.private_message(StateRule(RegisterState.wait_last_name_state))
async def handler_enter_last_name(message: Message):
    await save_user_data_in_db(message)
