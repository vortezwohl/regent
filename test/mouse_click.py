import logging

from ceo import Agent, get_openai_model

from regent.ability.mouse_click import mouse_click

logging.getLogger('ceo').setLevel(logging.DEBUG)

if __name__ == '__main__':
    agent = Agent([mouse_click], get_openai_model(), 'test')
    agent.assign('点击 [1763.0, 13.0]')
    agent.just_do_it()
