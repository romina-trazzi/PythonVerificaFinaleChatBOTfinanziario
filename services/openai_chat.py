import os
import requests
from dotenv import load_dotenv
load_dotenv()

print("✅ API KEY:", os.getenv("OPENROUTER_API_KEY"))

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Referer": "http://localhost:5000",
    "X-Title": "ChatbotFinanziario",
    "Content-Type": "application/json"
}

def ask_llm(message):
    url = "https://openrouter.ai/api/v1/chat/completions"
    model = "mistralai/mistral-small-3.2-24b-instruct:free"

    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": (
                    "Sei un assistente esperto di finanza. Dai risposte semplici, precise ed educate. "
                    "Evita argomenti non finanziari."
                )
            },
            {"role": "user", "content": message}
        ]
    }

    try:
        res = requests.post(url, headers=HEADERS, json=payload)
        res.raise_for_status()
        data = res.json()

        print("🪵 DEBUG - Risposta API:\n", data)  # 👈 AGGIUNTA PER DEBUG

        if "choices" in data:
            return data["choices"][0]["message"]["content"]
        else:
            return f"⚠️ Errore: risposta inattesa dall'API:\n{data}"

    except requests.exceptions.RequestException as e:
        return f"❌ Errore HTTP: {e}"
    except Exception as e:
        return f"❌ Errore generico: {e}"