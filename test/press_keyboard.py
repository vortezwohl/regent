import logging

from ceo import Agent, get_openai_model

from regent.ability.press_keyboard import (
    press_keyboard,
    press_keyboard_with_another_one_key_held_down,
    press_keyboard_with_another_two_keys_held_down,
    type_a_text
)

logging.getLogger('ceo').setLevel(logging.DEBUG)

if __name__ == '__main__':
    agent = Agent([
        press_keyboard,
        press_keyboard_with_another_one_key_held_down,
        press_keyboard_with_another_two_keys_held_down,
        type_a_text
    ],
        get_openai_model(), 'test')
    agent.assign('输入 alt + tab')
    agent.just_do_it()
