import cv2
import numpy as np
import pyautogui
import time
import win32gui
import win32api
import win32con
import DIKeys, hexKeyMap

enter_raid_image = cv2.imread('enter_raid.png')
enter_button_image = cv2.imread('enter_button.png')
ashava_found_image = cv2.imread('ashava_found.png')
ashava_dead_image = cv2.imread('ashava_dead.png')

threshold = 0.9
KEY1_INTERVAL = 7
KEY2_INTERVAL = 18
KEY3_INTERVAL = 10
KEY4_INTERVAL = 8
KEY5_INTERVAL = 23

def clickEnterRaid():

    while True:
        print('Enter Raid button is detecting...')
        time.sleep(1)

        screen_width1, screen_height1 = pyautogui.size()
        search_height1, search_width1, _ = enter_raid_image.shape
        search_range1 = (0, 0, screen_width1 - search_width1, screen_height1 - search_height1)

        screenshot1 = np.array(pyautogui.screenshot())
        gray_screenshot1 = cv2.cvtColor(screenshot1, cv2.COLOR_BGR2GRAY)
        result1 = cv2.matchTemplate(gray_screenshot1, cv2.cvtColor(enter_raid_image, cv2.COLOR_BGR2GRAY), cv2.TM_CCOEFF_NORMED)
        min_val1, max_val1, min_loc1, max_loc1 = cv2.minMaxLoc(result1)
        
        if max_val1 >= threshold:
            print('Match found with a rate of:', max_val1)
            win32gui.SetForegroundWindow(win32gui.FindWindow(None, "Diablo Immortal"))
            win32api.SetCursorPos((200, 300))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 200, 300, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 200, 300, 0, 0)
            print("Enter Raid button is clicked.")

            break
            
        search_range1 = (max_loc1[0], max_loc1[1], search_range1[2], search_range1[3])

def clickEnterButton():

    while True:
        print('Enter Button is detecting...')
        time.sleep(1)

        screen_width2, screen_height2 = pyautogui.size()
        search_height2, search_width2, _ = enter_button_image.shape
        search_range2 = (0, 0, screen_width2 - search_width2, screen_height2 - search_height2)

        screenshot2 = np.array(pyautogui.screenshot())
        gray_screenshot2 = cv2.cvtColor(screenshot2, cv2.COLOR_BGR2GRAY)
        result2 = cv2.matchTemplate(gray_screenshot2, cv2.cvtColor(enter_button_image, cv2.COLOR_BGR2GRAY), cv2.TM_CCOEFF_NORMED)
        min_val2, max_val2, min_loc2, max_loc2 = cv2.minMaxLoc(result2)
        
        if max_val2 >= threshold:
            print('Match found with a rate of:', max_val2)
            win32gui.SetForegroundWindow(win32gui.FindWindow(None, "Diablo Immortal"))
            win32api.SetCursorPos((1750, 780))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 1750, 780, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 1750, 780, 0, 0)
            print("Enter button is clicked.")

            break
            
        search_range2 = (max_loc2[0], max_loc2[1], search_range2[2], search_range2[3])

def moveCharacterToAshava():

    while True:
        print('Moving character to Ashava...')
        time.sleep(1)

        screen_width3, screen_height3 = pyautogui.size()
        search_height3, search_width3, _ = ashava_found_image.shape
        search_range3 = (0, 0, screen_width3 - search_width3, screen_height3 - search_height3)

        bossFound = True

        while bossFound:
            DIKeys.press(hexKeyMap.DIK_W) 
            DIKeys.KeyDown(hexKeyMap.DIK_W) # Press key
            screenshot3 = np.array(pyautogui.screenshot())
            gray_screenshot3 = cv2.cvtColor(screenshot3, cv2.COLOR_BGR2GRAY)
            result3 = cv2.matchTemplate(gray_screenshot3, cv2.cvtColor(ashava_found_image, cv2.COLOR_BGR2GRAY), cv2.TM_CCOEFF_NORMED)
            min_val3, max_val3, min_loc3, max_loc3 = cv2.minMaxLoc(result3)
            
            if max_val3 >= threshold:
                print('Match found with a rate of:', max_val3)
                print("Ashava is found.")
                DIKeys.KeyUp(hexKeyMap.DIK_W) # Release key
                DIKeys.press(hexKeyMap.DIK_W, 0.6) # Move a little towards the boss.
                bossFound = False
                break
            search_range3 = (max_loc3[0], max_loc3[1], search_range3[2], search_range3[3])
        break

def beginAttack():

    primary_attack_start_time = time.time()
    key1_last_time = 0
    key2_last_time = 0
    key3_last_time = 0
    key4_last_time = 0
    key5_last_time = 0

    time.sleep(4)
    DIKeys.press(hexKeyMap.DIK_1, 0.2)
    DIKeys.press(hexKeyMap.DIK_2, 0.2)
    DIKeys.press(hexKeyMap.DIK_3, 0.2)
    DIKeys.press(hexKeyMap.DIK_4, 0.2)

    while True:
        screen_width4, screen_height4 = pyautogui.size()
        search_height4, search_width4, _ = ashava_found_image.shape
        search_range4 = (0, 0, screen_width4 - search_width4, screen_height4 - search_height4)
        screenshot4 = np.array(pyautogui.screenshot())
        gray_screenshot4 = cv2.cvtColor(screenshot4, cv2.COLOR_BGR2GRAY)
        result4 = cv2.matchTemplate(gray_screenshot4, cv2.cvtColor(ashava_found_image, cv2.COLOR_BGR2GRAY), cv2.TM_CCOEFF_NORMED)
        min_val4, max_val4, min_loc4, max_loc4 = cv2.minMaxLoc(result4)

        if max_val4 >= threshold:
            # Spam the primary attack and use skills in the pre-defined intervals
            print('Attacking...')
            print('Match found with a rate of:', max_val4)

            DIKeys.KeyDown(hexKeyMap.DIK_SPACE)
            # DIKeys.press(hexKeyMap.DIK_1, 0.2)
            # DIKeys.press(hexKeyMap.DIK_2, 0.2)
            # DIKeys.press(hexKeyMap.DIK_3, 0.2)
            # DIKeys.press(hexKeyMap.DIK_4, 0.2)

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

            if time_elapsed - key5_last_time >= KEY5_INTERVAL:
                DIKeys.press(hexKeyMap.DIK_Q, 0.2) # Use the potion
                key5_last_time = time_elapsed
                    
            DIKeys.KeyUp(hexKeyMap.DIK_SPACE)

        screen_width5, screen_height5 = pyautogui.size()
        search_height5, search_width5, _ = ashava_dead_image.shape
        search_range5 = (0, 0, screen_width5 - search_width5, screen_height5 - search_height5)
        screenshot5 = np.array(pyautogui.screenshot())
        gray_screenshot5 = cv2.cvtColor(screenshot5, cv2.COLOR_BGR2GRAY)
        result5 = cv2.matchTemplate(gray_screenshot5, cv2.cvtColor(ashava_dead_image, cv2.COLOR_BGR2GRAY), cv2.TM_CCOEFF_NORMED)
        min_val5, max_val5, min_loc5, max_loc5 = cv2.minMaxLoc(result5)

        
        if max_val5 >=  threshold:
            print('Attacking is finished. Boss is dead.')
            print('Match found with a rate of:', max_val5)

            time.sleep(2)
            DIKeys.press(hexKeyMap.DIK_W, 1)
            time.sleep(2)
            DIKeys.press(hexKeyMap.DIK_E, 0.1)
            time.sleep(2)
            win32api.SetCursorPos((1150, 650))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 1150, 650, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 1150, 650, 0, 0)

            break

while True:
    if win32gui.FindWindow(None, "Diablo Immortal") == 0:
        print('Error: Diablo Immortal window not found.')

    time.sleep(2)
    clickEnterRaid()
    clickEnterButton()
    moveCharacterToAshava()
    beginAttack()
