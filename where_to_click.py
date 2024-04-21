# get where to go using locating the element. using ss or using the coordinates.
# if you are not using this package you can manually add coordinates to the click point.

# Main imports.
import pyautogui
import random
import time

#The imports I have already created. These are the packages that I have created inside these repository.

import m_movement

time.sleep(2)

# This function will return the center and size of the element as 2 tuples.
def get_center_and_size_of_the_element(image_path):
    element = pyautogui.locateOnScreen(image_path, confidence=0.9)

    center = (pyautogui.center(element).x, pyautogui.center(element).y)
    size = (element.height, element.width)
    print(center, size)

    return center, size


# this will return the click point inside the element once the center and the size is given.
def get_the_click_point(center, size):
    # Calculate the top left and bottom right coordinates
    top_left = (center[0] - size[0]/2, center[1] - size[1]/2)
    bottom_right = (center[0] + size[0]/2, center[1] + size[1]/2)

    # Generate a random point inside the box
    x = random.uniform(top_left[0], bottom_right[0])
    y = random.uniform(top_left[1], bottom_right[1])

    return (int(x), int(y))


# This function return the the click point. once you pass the top left corner and the box size.
def get_the_click_point(top_left, size):

    bottom_right = (top_left[0] + size[0], top_left[1] + size[1])

    x = random.uniform(top_left[0], bottom_right[0])
    y = random.uniform(top_left[1], bottom_right[1])

    return (int(x), int(y))

# This function will return the click point directly. We should give the values for them manually.
# Can be used pickpick tool to do that.

def get_the_click_point_directly(top, bottum, right, left):

    x = random.uniform(top[0], bottum[0])
    y = random.uniform(left[1], right[1])

    return (int(x), int(y))


click_point = get_the_click_point(get_center_and_size_of_the_element("file.png")[0], get_center_and_size_of_the_element("win11_2.png")[1])
print(click_point)
m_movement.go_to_point1_to_point2(m_movement.get_mouse_position(), click_point)