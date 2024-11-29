import logging

from ceo import Agent, get_openai_model

from regent.ability.press_keyboard import (
    press_a_key_with_another_one_key_held_down,
    press_a_key_with_another_two_keys_held_down,
    type_a_text
)

logging.getLogger('ceo').setLevel(logging.DEBUG)

if __name__ == '__main__':
    agent = Agent([
        press_a_key_with_another_one_key_held_down,
        press_a_key_with_another_two_keys_held_down,
        type_a_text
    ],
        get_openai_model(), 'test')
    agent.assign('键入 "abcd"')
    agent.just_do_it()
