import pyautogui
import time
import random

import get_click_point


from humancursor import SystemCursor


import pyautogui
import numpy as np
from pyclick import HumanClicker
import sys

time.sleep(5)


import keyboard


def stop_script(e):
    print("Script stopped")
    sys.exit()


keyboard.on_press_key("q", stop_script)


for x in range(10):

    # pyautogui.mouseDown()

    # initialize HumanClicker object
    hc = HumanClicker()

    # move the mouse to position (100,100) on the screen in approximately 2 seconds
    hc.move((100, 200), 5)

    # mouse click(left button)

    hc.move((1800, 800), 10)

    # pyautogui.mouseUp()


# time.sleep(15)
# for x in range(10):
#     pyautogui.mouseDown()
#     cursor = SystemCursor()
#     cursor.move_to([100, 200], duration=10)
#     cursor.move_to([1800, 800])
#     time.sleep(1)

# time.sleep(5)

# icon_position_x1 = 6
# icon_position_x2 = 86
# icon_position_y1 = 504
# icon_position_y2 = 570


# # take the position of the icon.

# icon_position = (
#     random.uniform(icon_position_x1, icon_position_x2),
#     random.uniform(icon_position_y1, icon_position_y2),
# )
# print(icon_position)


# pyautogui.moveTo(icon_position)

# pyautogui.doubleClick()

# time.sleep(10)

# create = pyautogui.locateCenterOnScreen("create_design.png")

# pyautogui.moveTo(create)
# pyautogui.click()

# print(icon_position)
