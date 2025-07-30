import sys
import os
import requests
from dotenv import load_dotenv

# 🔧 Aggiunge la cartella principale del progetto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from services.openai_chat import ask_llm

load_dotenv()

print("✅ Risposta:", ask_llm("Cos'è la borsa?"))

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