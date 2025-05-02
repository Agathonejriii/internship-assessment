import os
import requests
from dotenv import load_dotenv

load_dotenv()

url = "https://api.sunbird.ai/tasks/stt"
access_token = os.getenv("AUTH_TOKEN")
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {access_token}",
}

audio_path = "C:/Users/AGNES/Desktop/internship-assessment/AROMA_fixed.mp3"

with open(audio_path, "rb") as audio_file:
    files = {
        "audio": ("AROMA_fixed.mp3", audio_file, "audio/mpeg"),
    }
    data = {
        "language": "lug",
        "adapter": "lug",
        "whisper": True,
    }

    response = requests.post(url, headers=headers, files=files, data=data)
    print(response.status_code)
    print(response.json())
