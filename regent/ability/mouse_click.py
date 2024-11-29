import pyautogui
from ceo.util import ability


@ability
def mouse_click(x: int, y: int, clicks: int = 1) -> bool:
    pyautogui.click(x + 5, y + 5, clicks=clicks)
    return True
