import logging

from ceo import Agent, get_openai_model

from regent.ability.press_keyboard import (
    press_key,
    press_key_with_another_one_key_held_down,
    press_key_with_another_two_keys_held_down,
    type_input_text
)

logging.getLogger('ceo').setLevel(logging.DEBUG)

if __name__ == '__main__':
    agent = Agent([
        press_key,
        press_key_with_another_one_key_held_down,
        press_key_with_another_two_keys_held_down,
        type_input_text
    ],
        get_openai_model(), 'test')
    agent.assign('输入 win + r，然后 cmd，然后回车，然后输入dir，然后回车')
    agent.just_do_it()
