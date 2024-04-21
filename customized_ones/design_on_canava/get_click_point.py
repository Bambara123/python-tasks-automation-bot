import random
import time

print(time.time())


def generate_random_position_to_click(x1, x2, y1, y2):

    return (
        random.uniform(x1, x2),
        random.uniform(y1, y2),
    )

# def generate_random_time_typing():


