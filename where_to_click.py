# get where to go using locating the element.
# if you are not using this package you can manually add coordinates to the click point.


# Main imports.
import pyautogui
import random
import time

#The imports I have already created. These are the packages that I have created inside these repository.

import m_movement
import k_typing

time.sleep(2)

# This function will return the center and size of the element.
def get_center_and_size_of_the_element(image_path):
    element = pyautogui.locateOnScreen(image_path, confidence=0.9)

    center = (pyautogui.center(element).x, pyautogui.center(element).y)
    size = (element.height, element.width)

    return center, size

print(get_center_and_size_of_the_element("win11.png"))
