import json
import requests
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": f"Bearer {os.getenv('ENDPOINT')}"}

def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))

# raw_json = query({"inputs": input_text}) # function call
