from aiogram.utils.keyboard import KeyboardButton, ReplyKeyboardMarkup


def get_start_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Ввести баллы")],
            [KeyboardButton(text="Просмотреть баллы")],
        ],
        resize_keyboard=True,
        one_time_keyboard=True,
    )


def get_register_button():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Начать регистрацию")],
        ],
        resize_keyboard=True,
        one_time_keyboard=True,
    )
