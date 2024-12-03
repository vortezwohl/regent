import json

import pyautogui
from ceo.util import ability


@ability
def press_key(key: str) -> bool:
    pyautogui.press(key.lower())
    return True


@ability
def press_key_with_another_one_key_held_down(key: str, pre_held_key: str) -> bool:
    pyautogui.hotkey(pre_held_key.lower(), key.lower())
    return True


@ability
def press_key_with_another_two_keys_held_down(key: str, pre_held_key1: str, pre_held_key2: str) -> bool:
    pyautogui.hotkey(pre_held_key1.lower(), pre_held_key2.lower(), key.lower())
    return True


@ability
def write_text_with_keyboard(text: str) -> bool:
    # If you want to input a string or text
    # instead of press a single key, use this function.
    # For all single-char inputs, you must use [press_key]
    # instead of [write_text_with_keyboard].
    pyautogui.write(text)
    return True


additional_info = json.dumps({
    'keys_available': pyautogui.KEYBOARD_KEYS
}, ensure_ascii=False)

press_key.__doc__.join(additional_info)
press_key_with_another_one_key_held_down.__doc__.join(additional_info)
press_key_with_another_two_keys_held_down.__doc__.join(additional_info)
