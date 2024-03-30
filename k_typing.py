import pyautogui
import time
import random
import string
import ctypes


# make the time delay between key presses. between 0.3 and 1 seconds.
# for a long_delay, between 5 and 20 seconds.
def make_time_delay(normal_delay_percentage):
    long_delay = False

    long_delay = random.choices(
        [0, 1], weights=[normal_delay_percentage, 100 - normal_delay_percentage], k=1
    )[0]

    sleep_time = random.uniform(0.3, 1) if not long_delay else random.uniform(5, 20)

    time.sleep(sleep_time)
    print(sleep_time)


make_time_delay(90)


# imitate mistakes in typing.
def make_mistakes(last_letter):

    last_letter_upper = last_letter.isupper()

    print(last_letter_upper)

    amount_of_mistakes = random.randint(1, 3)

    for x in range(amount_of_mistakes):
        mistaken_char = random.choice(
            string.ascii_uppercase if last_letter_upper else string.ascii_lowercase
        )

        print(mistaken_char)
        pyautogui.typewrite(mistaken_char)
        make_time_delay()

    for x in range(amount_of_mistakes):
        pyautogui.press("backspace")
        make_time_delay()


# type letter 'x'


def type_letter_x(x):
    # Check if the letter is uppercase
    if x.isupper():
        # Check if Caps Lock is off
        if not is_capslock_on():
            # If it's off, turn it on
            pyautogui.press("capslock")
        # Type the letter
        pyautogui.press(x.lower())
    else:
        # Check if Caps Lock is on
        if is_capslock_on():
            # If it's on, turn it off
            pyautogui.press("capslock")
        # Type the letter
        pyautogui.press(x)


def is_capslock_on():
    hllDll = ctypes.WinDLL("User32.dll")
    VK_CAPITAL = 0x14
    return hllDll.GetKeyState(VK_CAPITAL)


# Test the function
print(type_letter_x("K"))
