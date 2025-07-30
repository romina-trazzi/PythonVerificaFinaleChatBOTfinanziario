import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
    "HTTP-Referer": "http://localhost:5000",
    "X-Title": "ChatbotFinanziario"
}

payload = {
    "model": "mistralai/mistral-small-3.2-24b-instruct:free",
    "messages": [
        {"role": "user", "content": "Cos'è la borsa?"}
    ]
}

res = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
print(res.status_code)
print(res.text)