import os
import requests
import json
from dotenv import load_dotenv

# Assicurati di caricare le variabili d'ambiente
load_dotenv()

def get_definition(term):
    api_key = os.getenv("OPENROUTER_API_KEY")
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:5000",  # Opzionale ma utile per il ranking
        "X-Title": "ChatbotFinanziario"          # Opzionale ma utile per il ranking
    }

    # Usa un modello gratuito più recente
    payload = {
        "model": "mistralai/mistral-small-3.2-24b-instruct:free",  # Modello aggiornato
        "messages": [
            {
                "role": "system",
                "content": "Fornisci una definizione breve e chiara di concetti finanziari."
            },
            {
                "role": "user",
                "content": f"Definisci: {term}"
            }
        ]
    }

    try:
        print(f"\n🔄 Invio richiesta a OpenRouter per definizione di: {term}")
        print(f"URL: {url}")
        print(f"Headers: {json.dumps(headers, indent=2)}")
        print(f"Payload: {json.dumps(payload, indent=2)}")
        
        response = requests.post(url, headers=headers, json=payload)
        
        print(f"\n📊 Status Code: {response.status_code}")
        print(f"📋 Response Headers: {dict(response.headers)}")
        print(f"📝 Response Text: {response.text[:500]}..." if len(response.text) > 500 else f"📝 Response Text: {response.text}")
        
        # Gestione degli errori HTTP
        if response.status_code != 200:
            return f"❌ Errore HTTP {response.status_code}: {response.text}"
        
        data = response.json()
        
        # Verifica che la risposta contenga i campi attesi
        if "choices" in data and len(data["choices"]) > 0 and "message" in data["choices"][0] and "content" in data["choices"][0]["message"]:
            return data["choices"][0]["message"]["content"].strip()
        else:
            return f"⚠️ Risposta ricevuta ma formato non valido: {data}"

    except requests.exceptions.RequestException as e:
        print(f"\n❌ Errore di connessione: {e}")
        return f"❌ Errore di connessione: {e}"
    except Exception as e:
        print(f"\n❌ Errore generico: {e}")
        return f"❌ Errore generico: {e}"