try:
    import pyautogui as p
except ImportError:
    import subprocess
    import pyautogui as p

import time
from typing import Tuple
from screen_scanner import ScreenScanner
from game_controller import GameController
from boss_killer import BossKiller

class Main:
    def __init__(self):
        self.screen_scanner = ScreenScanner()
        self.game_controller = GameController()
        self.boss_killer = BossKiller()

    def run(self):
        # Find and click the "Enter" button
        window = p.getWindowsWithTitle("Diablo Immortal")[0]
        window.activate()

        enter_button_location = self.screen_scanner.find_button(r"C:\Users\omer\Desktop\gpt-engineer-main\python\enter.png")
        if enter_button_location:
            self.game_controller.click_button(enter_button_location[0] + 135, enter_button_location[1] + 35)
        else:
            print("Failed to find the 'Enter' button. Exiting...")
            return

        # Wait for the game to load
        # time.sleep(10)

        # Move the character forward to the boss
        self.game_controller.press_key("W")
        boss_found = False
        while not boss_found:
            boss_found = self.screen_scanner.find_boss(r"C:\Users\omer\Desktop\gpt-engineer-main\python\ashava.png")
        self.game_controller.release_key("W")

        # Kill the boss
        self.boss_killer.kill_boss()

if __name__ == "__main__":
    main = Main()
    main.run()
