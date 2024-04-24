# capture numbers in range.
import pytesseract
import cv2
import numpy as np
import pyautogui
import re


# Path to the Tesseract executable (change this to your installation path)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Function to extract numbers from a given text

def extract_numbers(text):
    # Use regular expression to find the first number in the text
    match = re.search(r"[-+]?\d*\.\d+|\d+", text)
    if match:
        num = match.group()
        # Convert the number to float or int
        number = float(num) if '.' in num else int(num)
        return number
    else:
        return None


# Function to capture the screen and identify numbers in a specified region
def capture_screen_and_identify_numbers(region):
    # Capture the screen
    screenshot = pyautogui.screenshot(region=region)  
    screenshot_np = np.array(screenshot)
    screenshot_cv2 = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)

    extracted_text = pytesseract.image_to_string(screenshot_cv2)

    value = extract_numbers(extracted_text)

    return value
