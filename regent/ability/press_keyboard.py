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
    pyautogui.write(text)
    return True


additional_info = json.dumps({
    'keys_available': pyautogui.KEYBOARD_KEYS
}, ensure_ascii=False)

additional_info_type_input_text = json.dumps({
    'hint_for_type_input_text': 'If you want to input a string or text '
                                'instead of press a single key, use this function.'
}, ensure_ascii=False)

press_key.__doc__.join(additional_info)
press_key_with_another_one_key_held_down.__doc__.join(additional_info)
press_key_with_another_two_keys_held_down.__doc__.join(additional_info)
write_text_with_keyboard.__doc__.join(additional_info_type_input_text)
