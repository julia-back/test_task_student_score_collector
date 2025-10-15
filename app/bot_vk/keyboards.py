from vkbottle import Keyboard, Text


def start_keyboard():
    return (
        Keyboard(one_time=True, inline=False).add(Text("Ввести баллы")).row().add(Text("Просмотреть баллы"))
    ).get_json()


def register_button():
    return Keyboard(one_time=True, inline=False).add(Text("Начать регистрацию")).get_json()
