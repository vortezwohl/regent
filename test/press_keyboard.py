import logging

from ceo import Agent, get_openai_model, Personality
from regent.ability.press_keyboard import (
    press_key,
    press_key_with_another_one_key_held_down,
    press_key_with_another_two_keys_held_down,
    write_text_with_keyboard
)

logging.getLogger('ceo').setLevel(logging.DEBUG)
abilities = [press_key, press_key_with_another_one_key_held_down,
             press_key_with_another_two_keys_held_down, write_text_with_keyboard]

if __name__ == '__main__':
    agent = Agent(abilities=abilities, brain=get_openai_model(), name='test', personality=Personality.PRUDENT)
    agent.assign('press enter, type "hello world", then press enter again and type "this is reg"')
    agent.just_do_it()
