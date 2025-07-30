import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
print(f"API Key: {API_KEY[:5]}...")

# Configurazione minima
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

url = "https://openrouter.ai/api/v1/chat/completions"
model = "openai/gpt-3.5-turbo:free"

payload = {
    "model": model,
    "messages": [
        {"role": "user", "content": "Ciao"}
    ]
}

print("\nInvio richiesta...")
try:
    response = requests.post(url, headers=headers, json=payload)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
    
    if response.status_code == 200:
        print("\nSuccesso!")
    else:
        print("\nErrore!")
        
        # Prova con un altro modello
        print("\nProvo con un altro modello...")
        payload["model"] = "anthropic/claude-instant-1:free"
        response = requests.post(url, headers=headers, json=payload)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        
except Exception as e:
    print(f"Errore: {e}")