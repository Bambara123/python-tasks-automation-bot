from pyclick import HumanClicker
from humancursor import SystemCursor
import time
import pyautogui
import random


hc = HumanClicker()

x = 200.34
y = 1000

hc.move(x, y)

# # move the mouse to position (100,100) on the screen in approximately generated seconds
# hc.move(x, y)

pyautogui.moveTo(1000.67, 1000, duration=1.5)
