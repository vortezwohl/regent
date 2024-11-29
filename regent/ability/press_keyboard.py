import json

import pyautogui
from ceo.util import ability


@ability
def press_key(key: str) -> bool:
    pyautogui.press(key.lower())
    return True


@ability
def press_key_with_another_one_key_held_down(key: str, pre_held_key: str) -> bool:
    pyautogui.hotkey(pre_held_key, key)
    return True


@ability
def press_key_with_another_two_keys_held_down(key: str, pre_held_key1: str, pre_held_key2: str) -> bool:
    pyautogui.hotkey(pre_held_key1, pre_held_key2, key)
    return True


@ability
def type_input_text(text: str) -> bool:
    pyautogui.write(text)
    return True


additional_info_key = json.dumps({
    'keys_available': pyautogui.KEYBOARD_KEYS
}, ensure_ascii=False)

additional_info_hotkey = json.dumps({
    'keys_available': pyautogui.KEYBOARD_KEYS,
    'hint_for_hotkey_presses': 'Carefully think if user really wants a hotkey, '
                               'and seriously think the order of your operations.'
}, ensure_ascii=False)

additional_info_type_input_text = json.dumps({
    'hint_for_type_input_text': 'If you want to input more than one key, you want to input a string or text, use this function.'
}, ensure_ascii=False)

press_key.__doc__.join(additional_info_key)
press_key_with_another_one_key_held_down.__doc__.join(additional_info_hotkey)
press_key_with_another_two_keys_held_down.__doc__.join(additional_info_hotkey)
type_input_text.__doc__.join(additional_info_type_input_text)
