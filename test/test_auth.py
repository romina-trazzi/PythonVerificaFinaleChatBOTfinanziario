import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
print(f"API Key (primi 5 caratteri): {API_KEY[:5]}...")

# Test con diversi formati di header
header_formats = [
    {"Authorization": f"Bearer {API_KEY}"},
    {"Authorization": API_KEY},
    {"Authorization": f"Bearer {API_KEY}", "HTTP-Referer": "http://localhost:5000"},
    {"Authorization": f"Bearer {API_KEY}", "HTTP-Referer": "https://example.com"},
    {"Authorization": f"Bearer {API_KEY}", "HTTP-Referer": "http://localhost:5000", "X-Title": "ChatbotFinanziario"}
]

for i, headers in enumerate(header_formats):
    print(f"\n\nTest #{i+1} con headers: {headers}")
    
    try:
        # Test endpoint per i modelli (più semplice)
        response = requests.get("https://openrouter.ai/api/v1/models", headers=headers)
        print(f"Status Code: {response.status_code}")
        print(f"Risposta: {response.text[:200]}..." if len(response.text) > 200 else f"Risposta: {response.text}")
    except Exception as e:
        print(f"Errore: {e}")