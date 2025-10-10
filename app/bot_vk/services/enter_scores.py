from vkbottle.bot import Message
from bot_vk.states import EnterScoresState, state_dispenser
from database import DatabaseManager
from scores.models import Score
from users.models import User
from sqlalchemy import select


async def ask_subject_for_enter_scores(message: Message):
    await state_dispenser.set(message.from_id, EnterScoresState.wait_subject)
    await message.answer("Введите предмет, баллы которого хотите сохранить:")


async def cansel_enter_score(message: Message):
    await state_dispenser.delete(message.from_id)
    await message.answer("Сохранение предмета отменено.")


async def save_subject_ask_point_for_enter_score(message: Message):
    subject = message.text.strip()
    await state_dispenser.set(message.from_id, EnterScoresState.wait_point,
                              subject=subject)
    await message.answer("Введите баллы ЕГЭ для предмета:")


async def save_user_score_in_db(message: Message):
    point = message.text.strip()
    try:
        int(point)
    except ValueError:
        await message.answer("Балл должен быть целым числом. Попробуйте еще раз:")
        return

    if not (0 <= int(point) <= 100):
        await message.answer("Балл должен быть целым числом от 0 до 100.\n"
                             "Попробуйте еще раз:")
        return

    state = await state_dispenser.get(message.from_id)
    subject = state.payload.get("subject")

    user = None
    async for session in DatabaseManager.get_session():
        result = await session.execute(select(User).where(User.vk_id == message.from_id))
        user = result.scalar_one_or_none()

    if user:
        user_id = user.id
    else:
        await state_dispenser.delete(message.from_id)
        await message.answer("Пользоатель не зарегистрирован, пожалуйста, "
                             "пройдите регистрацию.")
        return

    score = Score(subject=subject, point=int(point), user_id=user_id)
    async for session in DatabaseManager.get_session():
        session.add(score)
        await session.commit()
        await session.refresh(score)

    await state_dispenser.delete(message.from_id)
    await message.answer("Баллы успешно сохранены.\n"
                         f"Предмет: {score.subject}\n"
                         f"Балл: {score.point}\n")
