import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
print(f"API Key (primi 5 caratteri): {API_KEY[:5]}...")

# Test con diversi formati di header per l'endpoint chat/completions
header_formats = [
    {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
    {"Authorization": f"Bearer {API_KEY}", "HTTP-Referer": "http://localhost:5000", "Content-Type": "application/json"},
    {"Authorization": f"Bearer {API_KEY}", "HTTP-Referer": "https://example.com", "Content-Type": "application/json"},
    {"Authorization": f"Bearer {API_KEY}", "HTTP-Referer": "http://localhost:5000", "X-Title": "ChatbotFinanziario", "Content-Type": "application/json"},
    # Prova con Referer invece di HTTP-Referer
    {"Authorization": f"Bearer {API_KEY}", "Referer": "http://localhost:5000", "Content-Type": "application/json"},
]

for i, headers in enumerate(header_formats):
    print(f"\n\nTest #{i+1} con headers: {headers}")
    
    try:
        url = "https://openrouter.ai/api/v1/chat/completions"
        # Prova con un modello diverso
        model = "openai/gpt-3.5-turbo:free"
        
        payload = {
            "model": model,
            "messages": [
                {"role": "user", "content": "Cos'è un'azione finanziaria? (rispondi brevemente)"}
            ]
        }
        
        response = requests.post(url, headers=headers, json=payload)
        print(f"Status Code: {response.status_code}")
        print(f"Response Headers: {response.headers}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"Risposta: Successo! Contiene 'choices': {'choices' in data}")
        else:
            print(f"Risposta: {response.text}")
    except Exception as e:
        print(f"Errore: {e}")