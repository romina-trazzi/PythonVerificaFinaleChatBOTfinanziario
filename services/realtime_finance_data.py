import requests
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

# Chiavi API (da aggiungere al file .env)
ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY", "")
STOCKDATA_API_KEY = os.getenv("STOCKDATA_API_KEY", "")

# Funzione per lo scraping di Google Finance
# Funzione per lo scraping di Google Finance
def get_google_finance_data(ticker):
    try:
        url = f"https://www.google.com/finance/quote/{ticker}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Stampa HTML per debug
        # print(soup.prettify())
        
        # Selettori aggiornati
        price_div = soup.select_one('div.YMlKec.fxKbKc')
        price = price_div.text if price_div else "N/A"
        
        # Estrazione della variazione
        change_div = soup.select_one('div.JwB6zf')
        change = change_div.text if change_div else "N/A"
        
        # Estrazione del nome del titolo
        name_div = soup.select_one('div.zzDege')
        name = name_div.text if name_div else ticker
        
        return {
            "source": "Google Finance",
            "name": name,
            "price": price,
            "change": change,
            "currency": "USD",
            "success": True
        }
    except Exception as e:
        print(f"Errore nello scraping di Google Finance: {e}")
        return {"success": False, "error": str(e)}
    

# Funzione per ottenere dati da Alpha Vantage
def get_alpha_vantage_data(ticker):
    try:
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey={ALPHA_VANTAGE_API_KEY}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        if "Global Quote" in data and data["Global Quote"]:
            quote = data["Global Quote"]
            return {
                "source": "Alpha Vantage",
                "name": ticker,
                "price": quote.get("05. price", "N/A"),
                "change": quote.get("10. change percent", "N/A"),
                "volume": quote.get("06. volume", "N/A"),
                "currency": "USD",
                "success": True
            }
        else:
            return {"success": False, "error": "Dati non disponibili"}
    except Exception as e:
        print(f"Errore nella chiamata a Alpha Vantage: {e}")
        return {"success": False, "error": str(e)}

# Funzione per ottenere dati da StockData
def get_stockdata_data(ticker):
    try:
        url = f"https://api.stockdata.org/v1/data/quote?symbols={ticker}&api_token={STOCKDATA_API_KEY}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        if "data" in data and data["data"]:
            quote = data["data"][0]
            return {
                "source": "StockData",
                "name": quote.get("name", ticker),
                "price": quote.get("price", "N/A"),
                "change": quote.get("day_change", "N/A"),
                "volume": quote.get("volume", "N/A"),
                "currency": quote.get("currency", "USD"),
                "success": True
            }
        else:
            return {"success": False, "error": "Dati non disponibili"}
    except Exception as e:
        print(f"Errore nella chiamata a StockData: {e}")
        return {"success": False, "error": str(e)}

# Funzione principale che prova diverse fonti in ordine
# Funzione principale che prova diverse fonti in ordine
def get_realtime_data(ticker):
    # Normalizza il ticker per Google Finance (aggiunge :NASDAQ se necessario)
    google_ticker = ticker
    if ":" not in ticker:
        google_ticker = f"{ticker}:NASDAQ"
    
    # Prima prova con lo scraping di Google Finance
    data = get_google_finance_data(google_ticker)
    if data["success"] and data["price"] != "N/A":
        return data
    
    # Se fallisce, prova con Alpha Vantage
    if ALPHA_VANTAGE_API_KEY:
        data = get_alpha_vantage_data(ticker)
        if data["success"] and data["price"] != "N/A":
            return data
    
    # Se fallisce ancora, prova con StockData
    if STOCKDATA_API_KEY:
        data = get_stockdata_data(ticker)
        if data["success"] and data["price"] != "N/A":
            return data
    
    # Se tutte le fonti falliscono, restituisci un errore
    return {"success": False, "error": "Non è stato possibile ottenere dati in tempo reale da nessuna fonte"}