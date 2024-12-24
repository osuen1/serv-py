import requests
from dotenv import load_dotenv
import os

load_dotenv()
url = os.getenv('API_URL')
token = os.getenv('TOKEN')
headers = {
    "Authorization": f"Bearer {token}"
}

def query(message):
    payload = {
        'inputs': message
    }

    response = requests.post(url=url, headers=headers, json=payload)
    return response.json()