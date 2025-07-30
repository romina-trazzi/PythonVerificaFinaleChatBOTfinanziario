import os
import requests
from dotenv import load_dotenv

load_dotenv()  # carica la API key da .env

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
if not OPENROUTER_API_KEY:
    print("❌ OPENROUTER_API_KEY non trovata nel file .env")
    exit()

HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "HTTP-Referer": "http://localhost:5000",
    "X-Title": "ChatbotFinanziario"
}

def test_api_key():
    url = "https://openrouter.ai/api/v1/chat/completions"
    model = "mistralai/mistral-small-3.2-24b-instruct:free"  # puoi cambiare con un altro modello free

    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": "Spiegami cos'è un'azione finanziaria"}
        ]
    }

    print("🔍 Test in corso...\n")

    try:
        response = requests.post(url, headers=HEADERS, json=payload)
        print("✅ Status Code:", response.status_code)
        data = response.json()
        print("📦 Risposta ricevuta:\n", data)

        if "choices" in data:
            print("\n✅ Risposta corretta dal modello:\n")
            print(data["choices"][0]["message"]["content"])
        else:
            print("\n❌ Errore: la risposta non contiene 'choices'")
            print("Contenuto completo:", data)

    except Exception as e:
        print(f"\n❌ Eccezione durante la richiesta: {e}")

if __name__ == "__main__":
    test_api_key()