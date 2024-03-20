import pyautogui
import time

time.sleep(5)

pyautogui.click(100, 100)

icon_position = pyautogui.locateOnScreen("icon.png")

# print(icon_position)
