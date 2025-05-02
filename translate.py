import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define the URL for the translation endpoint
url = "https://api.sunbird.ai/tasks/nllb_translate"

# Load the access token from .env file
access_token = os.getenv("AUTH_TOKEN")

# Check if the token is loaded correctly
if not access_token:
    print("Error: AUTH_TOKEN not found in .env file")
    exit(1)

# Define the headers for the API request
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {access_token}",  # Using the token from .env
    "Content-Type": "application/json",
}

# Define the translation request data
data = {
    "source_language": "lug",  # Source language (Luganda)
    "target_language": "eng",  # Target language (English)
    "text": "Ekibiina ekiddukanya omuzannyo gw’emisinde mu ggwanga ekya Uganda Athletics Federation kivuddeyo nekitegeeza nga lawundi esooka eyemisinde egisunsulamu abaddusi abanakiika mu mpaka ezenjawulo ebweru w’eggwanga egya National Athletics Trials nga bwegisaziddwamu.",
}

# Make the POST request to the translation API
response = requests.post(url, headers=headers, json=data)

# Print the full response to check the content
print("Response JSON:", response.json())

# Check the response status
if response.status_code == 200:
    # Access translated text from the response output
    translated_text = response.json().get("output", {}).get("translated_text")
    if translated_text:
        print("Translated Text:", translated_text)
    else:
        print("Error: Translated text not found in the response.")
else:
    # Print error message if the request was not successful
    print("Error:", response.status_code, response.text)

