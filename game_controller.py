import pyautogui

class GameController:
    def click_button(self, x: int, y: int) -> None:
        # Simulate a mouse click at the specified coordinates
        pyautogui.click(x, y)

    def press_key(self, key: str) -> None:
        # Simulate pressing a key
        pyautogui.keyDown(key)

    def release_key(self, key: str) -> None:
        # Simulate releasing a key
        pyautogui.keyUp(key)
