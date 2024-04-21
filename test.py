# capture all text in a specific range. - > customize to numbers

import pytesseract
import cv2
import numpy as np
import pyautogui

import time

# Path to the Tesseract executable (change this to your installation path)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def capture_screen_and_identify_numbers(region):
    # Capture the screen
    screenshot = pyautogui.screenshot(region=region)
    # Convert the screenshot to a format compatible with Tesseract
    screenshot_np = np.array(screenshot)
    screenshot_cv2 = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)
    # Use Tesseract to extract text from the screenshot
    extracted_text = pytesseract.image_to_string(screenshot_cv2)
    # Filter out non-numeric characters and convert to integers
    numbers = [int(word) for word in extracted_text.split() if word.isdigit()]
    return extracted_text

time.sleep(3)
# Define the region of the screen to capture (left, top, width, height)
region = (106, 613, 283, 98)

# Call the function to capture the screen and identify numbers in the specified region
numbers = capture_screen_and_identify_numbers(region)
print("Numbers identified in the specified region:", numbers)
