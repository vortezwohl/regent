import json

import pyautogui
from ceo.util import ability


@ability
def press_key_with_another_one_key_held_down(key: str, pre_held_key: str) -> bool:
    pyautogui.hotkey(pre_held_key, key)
    return True


@ability
def press_key_with_another_two_keys_held_down(key: str, pre_held_key1: str, pre_held_key2: str) -> bool:
    pyautogui.hotkey(pre_held_key1, pre_held_key2, key)
    return True


@ability
def type_text(text: str) -> bool:
    pyautogui.write(text)
    return True


additional_info = json.dumps({
    'keys_available': pyautogui.KEYBOARD_KEYS,
    'hint_for_hotkey_presses': 'Carefully think if user really wants a hotkey, '
                               'and seriously think the '
}, ensure_ascii=False)

press_key_with_another_one_key_held_down.__doc__.join(additional_info)
press_key_with_another_two_keys_held_down.__doc__.join(additional_info)
