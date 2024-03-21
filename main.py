import pyautogui
import time
import random

import get_click_point

time.sleep(5)

icon_position_x1 = 6
icon_position_x2 = 86
icon_position_y1 = 504
icon_position_y2 = 570


# take the position of the icon.

icon_position = (
    random.uniform(icon_position_x1, icon_position_x2),
    random.uniform(icon_position_y1, icon_position_y2),
)
print(icon_position)


pyautogui.moveTo(icon_position)

pyautogui.doubleClick()

time.sleep(10)

create = pyautogui.locateCenterOnScreen("create_design.png")

pyautogui.moveTo(create)
pyautogui.click()

print(icon_position)
