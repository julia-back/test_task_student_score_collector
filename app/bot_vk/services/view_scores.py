from vkbottle.bot import Message
from bot_vk.states import ViewScoresState, state_dispenser
from users.models import User
from database import DatabaseManager
from sqlalchemy import select
from sqlalchemy.orm import selectinload


async def ask_subject_for_view_scores(message: Message):
    await state_dispenser.get(message.from_id, ViewScoresState.wait_subject)
    await message.answer("Введите предмет, по которому необходимо посмотреть баллы:"
                         "(или введите 'все' для просмотра всех баллов)")


async def view_user_scores(message: Message):
    subject = message.text.strip()

    user = None
    async for session in DatabaseManager.get_session():
        result = await session.execute(select(User)
                                       .options(selectinload(User.scores))
                                       .where(User.vk_id == message.from_id))
        user = result.scalar_one_or_none()

    user_scores = None
    if user:
        if subject.lower() == "все":
            user_scores = user.scores
        else:
            user_scores = [score for score in user.scores
                           if score.subject.lower() == subject.lower()]
    else:
        await state_dispenser.delete(message.from_id)
        await message.answer("Пользователь не зарегистрирован.")

    if not user_scores:
        await message.answer("Предмет не найден, попробуйте еще раз:")
        return

    text = "Ваши баллы:"
    for score in user_scores:
        text += f"\n{str(score.subject).title()} - {score.point}"

    await state_dispenser.delete(message.from_id)
    await message.answer(text=text)
