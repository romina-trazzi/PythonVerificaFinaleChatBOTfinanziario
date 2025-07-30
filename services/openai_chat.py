import os
import requests
import json
from dotenv import load_dotenv
load_dotenv()

print("✅ API KEY:", os.getenv("OPENROUTER_API_KEY")[:5] + "..." if os.getenv("OPENROUTER_API_KEY") else "Non trovata")

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Aggiornamento degli header in base all'esempio
HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "HTTP-Referer": "http://localhost:5000",  # Opzionale ma utile per il ranking
    "X-Title": "ChatbotFinanziario",         # Opzionale ma utile per il ranking
    "Content-Type": "application/json"
}

def ask_llm(message):
    url = "https://openrouter.ai/api/v1/chat/completions"
    # Aggiornamento del modello in base all'esempio
    model = "openai/gpt-4o"  # Modello aggiornato dall'esempio

    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": 
                    "Sei un assistente esperto di finanza. Dai risposte semplici, precise ed educate. "
                    "Evita argomenti non finanziari."
                
            },
            {"role": "user", "content": message}
        ],
        "temperature": 0.7,
        "max_tokens": 150
    }

    try:
        print("\n🔄 Invio richiesta a OpenRouter...")
        print(f"URL: {url}")
        print(f"Headers: {json.dumps(HEADERS, indent=2)}")
        print(f"Payload: {json.dumps(payload, indent=2)}")
        
        res = requests.post(url, headers=HEADERS, json=payload)
        
        print(f"\n📊 Status Code: {res.status_code}")
        print(f"📋 Response Headers: {dict(res.headers)}")
        print(f"📝 Response Text: {res.text[:500]}..." if len(res.text) > 500 else f"📝 Response Text: {res.text}")
        
        # Non usare raise_for_status qui per gestire manualmente gli errori
        if res.status_code == 200:
            data = res.json()
            print("\n✅ Risposta ricevuta con successo!")
            print("🪵 DEBUG - Risposta API:\n", data)  # Spostato qui per evitare errori
            
            if "choices" in data and len(data["choices"]) > 0:
                return data["choices"][0]["message"]["content"]
            else:
                return f"⚠️ Risposta ricevuta ma formato non valido: {data}"
        else:
            return f"❌ Errore HTTP {res.status_code}: {res.text}"
            
    except requests.exceptions.RequestException as e:
        print(f"\n❌ Errore di connessione: {e}")
        return f"❌ Errore di connessione: {e}"
    except Exception as e:
        print(f"\n❌ Errore generico: {e}")
        return f"❌ Errore generico: {e}"