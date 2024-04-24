import read_number_or_float as rnf
import time

region = (244, 613, 141, 57)


time.sleep(3)

numbers = rnf.capture_screen_and_identify_numbers(region)
print("Numbers identified in the specified region:", numbers)
