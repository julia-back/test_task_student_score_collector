from vkbottle import BaseStateGroup


class RegisterState(BaseStateGroup):

    wait_username_state = "wait_username"
    wait_first_name_state = "wait_first_name"
    wait_last_name_state = "wait_last_name"


class EnterScoresState(BaseStateGroup):

    wait_subject = "wait_subject"
    wait_point = "wait_point"


class ViewScoresState(BaseStateGroup):

    wait_subject = "wait_subject"
