from aiogram.fsm.state import State, StatesGroup


class RegistrationStates(StatesGroup):

    wait_for_username = State()
    wait_for_first_name = State()
    wait_for_last_name = State()


class ViewScoresState(StatesGroup):

    wait_subject = State()


class EnterScoreState(StatesGroup):

    wait_subject = State()
    wait_score = State()
