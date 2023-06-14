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
ENTER_RAID_PATH = r'C:\Users\omer\Desktop\gpt-engineer-main\python\enter_raid.png'
ENTER_RAID_PATH2 = r'C:\Users\omer\Desktop\gpt-engineer-main\python\enter_raid_2.png'
EXIT_RAID_PATH = r'C:\Users\omer\Desktop\gpt-engineer-main\python\exit_raid.png'

MATCH_THRESHOLD = 0.9
MATCH_THRESHOLD_ASHAVA = 0.6
MATCH_THRESHOLD_FIND_RAID = 0.25
MATCH_THRESHOLD_EXIT_RAID = 0.4

# Define the key press intervals in seconds
KEY1_INTERVAL = 10
KEY2_INTERVAL = 21
KEY3_INTERVAL = 13
KEY4_INTERVAL = 10
KEY4_INTERVAL = 25

# Load the image files for button and text matching
enter_button_template = cv2.imread(ENTER_BUTTON_PATH, cv2.COLOR_BGR2GRAY)
ashava_text_template = cv2.imread(ASHAVA_TEXT_PATH, cv2.COLOR_BGR2GRAY)
enter_raid_template = cv2.imread(ENTER_RAID_PATH, cv2.COLOR_BGR2GRAY)
enter_raid_template2 = cv2.imread(ENTER_RAID_PATH2, cv2.COLOR_BGR2GRAY)
exit_raid_template = cv2.imread(EXIT_RAID_PATH, cv2.COLOR_BGR2GRAY)

while True:

    while True: 
        # Find the Enter button
        hwnd = win32gui.FindWindow(None, "Diablo Immortal")
        if hwnd == 0:
            print('Error: Diablo Immortal window not found.')
            exit()

        time.sleep(6)

        rect = win32gui.GetWindowRect(hwnd)
        x, y = rect[0], rect[1]
        w, h = rect[2] - x, rect[3] - y

        screen = np.array(pyautogui.screenshot(region=(x, y, w, h)))
        enter_raid_match = cv2.matchTemplate(screen, enter_raid_template, cv2.TM_CCOEFF_NORMED)
        enter_raid_location = np.where(enter_raid_match >= MATCH_THRESHOLD_FIND_RAID)
        if enter_raid_location[0].size > 0:
            print('Enter button found.')
            time.sleep(2)
            enter_button_x = 200
            enter_button_y = 300
            win32gui.SetForegroundWindow(hwnd)
            win32api.SetCursorPos((enter_button_x, enter_button_y))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, enter_button_x, enter_button_y, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, enter_button_x, enter_button_y, 0, 0)
            break
        else:
            print('Raid not found.')
            time.sleep(1)

    # Define the loop that searches for the button and text
    while True:
        rect = win32gui.GetWindowRect(hwnd)
        x, y = rect[0], rect[1]
        w, h = rect[2] - x, rect[3] - y

        screen = np.array(pyautogui.screenshot(region=(x, y, w, h)))
        enter_button_match = cv2.matchTemplate(screen, enter_button_template, cv2.TM_CCOEFF_NORMED)
        enter_button_location = np.where(enter_button_match >= MATCH_THRESHOLD)
        if enter_button_location[0].size > 0:
            # Click the Enter buttons
            enter_button_x = 1670
            enter_button_y = 780
            win32api.SetCursorPos((enter_button_x, enter_button_y))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, enter_button_x, enter_button_y, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, enter_button_x, enter_button_y, 0, 0)
            break
        else:
            print('Enter button not found.')
            time.sleep(1)

    # Wait for the game to load
    time.sleep(6)

    # Move the character to the boss
    while True:
        rect = win32gui.GetWindowRect(hwnd)
        x, y = rect[0], rect[1]
        w, h = rect[2] - x, rect[3] - y

        screen = np.array(pyautogui.screenshot(region=(x, y, w, h)))
        ashava_text_match = cv2.matchTemplate(screen, ashava_text_template, cv2.TM_CCOEFF_NORMED)
        ashava_text_location = np.where(ashava_text_match >= MATCH_THRESHOLD_ASHAVA)
        if ashava_text_location[0].size > 0:
            print('ASHAVA FOUND.')
            DIKeys.press(hexKeyMap.DIK_W, 1.5)      
            break

        else:
            if ashava_text_location[0].size > 0:
                print('ASHAVA FOUND.')
                DIKeys.press(hexKeyMap.DIK_W, 1.5) 
                break

        DIKeys.press(hexKeyMap.DIK_W, 0.5)      

    # Spam the primary attack and use the other keys in the pre-defined intervals
    primary_attack_start_time = time.time()
    key1_last_time = 0
    key2_last_time = 0
    key3_last_time = 0
    key4_last_time = 0
    key5_last_time = 0

    while True:
        rect = win32gui.GetWindowRect(hwnd)
        x, y = rect[0], rect[1]
        w, h = rect[2] - x, rect[3] - y

        screen = np.array(pyautogui.screenshot(region=(x, y, w, h)))
        ashava_text_match = cv2.matchTemplate(screen, ashava_text_template, cv2.TM_CCOEFF_NORMED)
        ashava_text_location = np.where(ashava_text_match >= MATCH_THRESHOLD_ASHAVA)
        if ashava_text_location[0].size > 0:
            # Spam the primary attack
            DIKeys.KeyDown(hexKeyMap.DIK_SPACE)

            DIKeys.press(hexKeyMap.DIK_1, 0.2)
            DIKeys.press(hexKeyMap.DIK_2, 0.2)
            DIKeys.press(hexKeyMap.DIK_3, 0.2)
            DIKeys.press(hexKeyMap.DIK_4, 0.2)

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
            if time_elapsed - key5_last_time >= KEY4_INTERVAL:
                DIKeys.press(hexKeyMap.DIK_Q, 0.2) # Use the potion
                key5_last_time = time_elapsed
            
            DIKeys.KeyUp(hexKeyMap.DIK_SPACE)

        else:
            time.sleep(2)
            DIKeys.press(hexKeyMap.DIK_W, 2)
            break

    while True: 
        time.sleep(1)

        rect = win32gui.GetWindowRect(hwnd)
        x, y = rect[0], rect[1]
        w, h = rect[2] - x, rect[3] - y

        screen = np.array(pyautogui.screenshot(region=(x, y, w, h)))
        exit_button_match = cv2.matchTemplate(screen, exit_raid_template, cv2.TM_CCOEFF_NORMED)
        exit_button_location = np.where(exit_button_match >= MATCH_THRESHOLD_FIND_RAID)
        if exit_button_location[0].size > 0:
            # Click the Enter button
            enter_button_x = 1570
            enter_button_y = 140
            win32gui.SetForegroundWindow(hwnd)
            win32api.SetCursorPos((enter_button_x, enter_button_y))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, enter_button_x, enter_button_y, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, enter_button_x, enter_button_y, 0, 0)

            time.sleep(1.5)
            enter_button_x = 1150
            enter_button_y = 650
            win32api.SetCursorPos((enter_button_x, enter_button_y))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, enter_button_x, enter_button_y, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, enter_button_x, enter_button_y, 0, 0)
            time.sleep(6)
            break
        else:
            print('Raid not found.')
            time.sleep(1)       
    

    
