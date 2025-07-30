import os
import requests
import json
from dotenv import load_dotenv

# Carica le variabili d'ambiente
load_dotenv()

# Ottieni la chiave API
API_KEY = os.getenv("OPENROUTER_API_KEY")
print(f"API Key: {API_KEY[:5]}..." if API_KEY else "API Key non trovata")

# Test della validità della chiave API
def test_api_key():
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    # Verifica i modelli disponibili
    response = requests.get("https://openrouter.ai/api/v1/models", headers=headers)
    
    print(f"Status code: {response.status_code}")
    print(f"Response: {response.text[:200]}..." if len(response.text) > 200 else f"Response: {response.text}")
    
    if response.status_code == 200:
        data = response.json()
        print("\nModelli gratuiti disponibili:")
        for model in data["data"]:
            model_id = model.get("id", "")
            if ":free" in model_id:
                print(f"- {model_id}")
        return True
    else:
        print(f"Errore: {response.text}")
        return False

# Test di una richiesta semplice
def test_simple_request():
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "mistralai/mistral-small-3.2-24b-instruct:free",
        "messages": [
            {"role": "user", "content": "Cos'è la finanza?"}
        ]
    }
    
    print("\nInvio richiesta a OpenRouter...")
    print(f"Headers: {json.dumps(headers, indent=2)}")
    print(f"Payload: {json.dumps(payload, indent=2)}")
    
    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
    
    print(f"\nTest richiesta semplice - Status code: {response.status_code}")
    print(f"Response: {response.text[:200]}..." if len(response.text) > 200 else f"Response: {response.text}")
    
    if response.status_code == 200:
        data = response.json()
        if "choices" in data and len(data["choices"]) > 0:
            print(f"Risposta: {data['choices'][0]['message']['content'][:100]}...")
            return True
    
    print(f"Errore: {response.text}")
    return False

# Esegui i test
if __name__ == "__main__":
    print("\n=== Test validità chiave API ===")
    api_key_valid = test_api_key()
    
    if api_key_valid:
        print("\n=== Test richiesta semplice ===")
        test_simple_request()