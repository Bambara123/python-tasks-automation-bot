# get where to go using locating the element.
# if you are not using this package you can manually add coordinates to the click point.

import pyautogui
import random


element = pyautogui.locateOnScreen("win.png")

# print(element.x, element.y)
print(element.height, element.width)
