from dotenv import load_dotenv
import os

import google.generativeai as genai
import os


# Load the .env file
load_dotenv()

BARD_API_KEY = os.getenv('BARD_API_KEY_')

# Configure the API key
genai.configure(api_key=BARD_API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')

response = model.generate_content("Give me 5 quites to create t-shirt designs line by line")
print(response.text)
