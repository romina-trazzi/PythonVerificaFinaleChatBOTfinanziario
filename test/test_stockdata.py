import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Carica la chiave API
STOCKDATA_API_KEY = os.getenv("STOCKDATA_API_KEY", "")
print(f"StockData API Key: {STOCKDATA_API_KEY[:5]}...")

# Test dell'API StockData
def test_stockdata_api():
    ticker = "AAPL"
    url = f"https://api.stockdata.org/v1/data/quote?symbols={ticker}&api_token={STOCKDATA_API_KEY}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        print("Risposta API StockData:")
        print(data)
        
        if "data" in data and data["data"]:
            quote = data["data"][0]
            print(f"Nome: {quote.get('name')}")
            print(f"Prezzo: {quote.get('price')}")
            print(f"Variazione: {quote.get('day_change')}")
            return True
        else:
            print("Dati non disponibili")
            return False
    except Exception as e:
        print(f"Errore nella chiamata a StockData: {e}")
        return False

if __name__ == "__main__":
    test_stockdata_api()