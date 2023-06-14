import cv2
import numpy as np
import pyautogui
import time
import win32gui
import win32api
import win32con
import DIKeys, hexKeyMap


# Define the path to the image files and the image matching threshold
ENTER_BUTTON_PATH = r'C:\Users\omer\Desktop\gpt-engineer-main\python\enter.png'
ASHAVA_TEXT_PATH = r'C:\Users\omer\Desktop\gpt-engineer-main\python\ashava.png'
MATCH_THRESHOLD = 0.9

# Define the key press intervals in seconds
KEY1_INTERVAL = 10
KEY2_INTERVAL = 21
KEY3_INTERVAL = 13
KEY4_INTERVAL = 10

# Define the screen region to search for the buttons and text
SCREEN_REGION = (1610, 749, 270, 70)

# Load the image files for button and text matching
enter_button_template = cv2.imread(ENTER_BUTTON_PATH, cv2.COLOR_BGR2GRAY)
ashava_text_template = cv2.imread(ASHAVA_TEXT_PATH, cv2.COLOR_BGR2GRAY)

# Define the key presses for spamming the primary attack
PRIMARY_ATTACK_KEY = 'space'

# Define the loop that searches for the button and text
while True:
    # Find the Enter button
    hwnd = win32gui.FindWindow(None, "Diablo Immortal")
    if hwnd == 0:
        print('Error: Diablo Immortal window not found.')
        exit()

    rect = win32gui.GetWindowRect(hwnd)
    x, y = rect[0], rect[1]
    w, h = rect[2] - x, rect[3] - y

    screen = np.array(pyautogui.screenshot(region=(x, y, w, h)))
    enter_button_match = cv2.matchTemplate(screen, enter_button_template, cv2.TM_CCOEFF_NORMED)
    enter_button_location = np.where(enter_button_match >= MATCH_THRESHOLD)
    if enter_button_location[0].size > 0:
        # Click the Enter button
        enter_button_x = 1670
        enter_button_y = 780
        win32gui.SetForegroundWindow(hwnd)
        win32api.SetCursorPos((enter_button_x, enter_button_y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, enter_button_x, enter_button_y, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, enter_button_x, enter_button_y, 0, 0)
        break
    else:
        print('Enter button not found.')
        time.sleep(1)

# Wait for the game to loadW
time.sleep(6)

# Move the character to the boss
while True:
    rect = win32gui.GetWindowRect(hwnd)
    x, y = rect[0], rect[1]
    w, h = rect[2] - x, rect[3] - y

    screen = np.array(pyautogui.screenshot(region=(x, y, w, h)))
    ashava_text_match = cv2.matchTemplate(screen, ashava_text_template, cv2.TM_CCOEFF_NORMED)
    ashava_text_location = np.where(ashava_text_match >= MATCH_THRESHOLD)
    if ashava_text_location[0].size > 0:
        print('ASHAVA FOUND.')
        break

    else:
        if ashava_text_location[0].size > 0:
            print('ASHAVA FOUND.')
            break

        DIKeys.press(hexKeyMap.DIK_W, 0.2)      

# Spam the primary attack and use the other keys in the pre-defined intervals
primary_attack_start_time = time.time()
print(primary_attack_start_time)
key1_last_time = 0
key2_last_time = 0
key3_last_time = 0
key4_last_time = 0

while True:
    screen = np.array(pyautogui.screenshot(region=(888, 15, 140, 30)))
    ashava_text_match = cv2.matchTemplate(screen, ashava_text_template, cv2.TM_CCOEFF_NORMED)
    ashava_text_location = np.where(ashava_text_match >= MATCH_THRESHOLD)
    if ashava_text_location[0].size > 0:
        # Spam the primary attack
        DIKeys.KeyDown(hexKeyMap.DIK_SPACE)

    
        # Check the intervals for Key 1 to 4
        time_elapsed = time.time() - primary_attack_start_time
        if time_elapsed - key1_last_time >= KEY1_INTERVAL:
            DIKeys.press(hexKeyMap.DIK_1, 0.2)
            key1_last_time = time_elapsed
        if time_elapsed - key2_last_time >= KEY2_INTERVAL:
            DIKeys.press(hexKeyMap.DIK_2, 0.2)
            key2_last_time = time_elapsed
        if time_elapsed - key3_last_time >= KEY3_INTERVAL:
            DIKeys.press(hexKeyMap.DIK_3, 0.2)
            key3_last_time = time_elapsed
        if time_elapsed - key4_last_time >= KEY4_INTERVAL:
            DIKeys.press(hexKeyMap.DIK_4, 0.2)
            key4_last_time = time_elapsed
        
        DIKeys.KeyUp(hexKeyMap.DIK_SPACE)

    #else:
        #break

print('Boss killed.')
