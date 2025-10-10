from vkbottle.bot import BotLabeler, Message
from vkbottle.dispatch.rules.base import CommandRule, StateRule, StateGroupRule
from bot_vk.states import RegisterState
from bot_vk.services.register import (start_register_ask_username, cansel_register,
                                      check_and_save_username, ask_first_name,
                                      save_first_name, ask_last_name,
                                      save_last_name, save_user_data_in_db)


labeler = BotLabeler()


@labeler.private_message(CommandRule("register", prefixes=["!", "/"]))
async def handler_register(message: Message):
    await start_register_ask_username(message)


@labeler.private_message(CommandRule("cansel", prefixes=["!", "/"]),
                         StateGroupRule(RegisterState))
async def handler_cansel_register(message: Message):
    await cansel_register(message)


@labeler.private_message(StateRule(RegisterState.wait_username_state))
async def handler_enter_username(message: Message):
    is_done = await check_and_save_username(message)
    if is_done:
        await ask_first_name(message)


@labeler.private_message(StateRule(RegisterState.wait_first_name_state))
async def handler_enter_first_name(message: Message):
    is_done = await save_first_name(message)
    if is_done:
        await ask_last_name(message)


@labeler.private_message(StateRule(RegisterState.wait_last_name_state))
async def handler_enter_last_name(message: Message):
    is_done = await save_last_name(message)
    if is_done:
        await save_user_data_in_db(message)
