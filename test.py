import pyautogui
import time
import random
import string


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


# make_mistakes("l")
        
# mouse movements
        

