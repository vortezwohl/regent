import logging

from ceo import Agent, get_openai_model
from regent.ability.press_keyboard import (
    press_key,
    press_key_with_another_one_key_held_down,
    press_key_with_another_two_keys_held_down,
    write_text_with_keyboard
)

logging.getLogger('ceo').setLevel(logging.DEBUG)


if __name__ == '__main__':
    agent = Agent([
        press_key,
        press_key_with_another_one_key_held_down,
        press_key_with_another_two_keys_held_down,
        write_text_with_keyboard
    ],
        get_openai_model(), 'test')
    agent.assign('输入五个enter，然后输入"nb"')
    agent.just_do_it()
