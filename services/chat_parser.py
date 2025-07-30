import requests
import os
from fuzzywuzzy import fuzz
import re

def interpret_message(message):
    message = message.lower()

    # Riconoscimento di richieste di dati in tempo reale
    realtime_patterns = [
        r"dati\s+(?:in\s+)?tempo\s+reale\s+(?:per|di)\s+([a-zA-Z0-9.]+)",
        r"informazioni\s+(?:in\s+)?tempo\s+reale\s+(?:per|di)\s+([a-zA-Z0-9.]+)",
        r"(?:prezzo|quotazione)\s+(?:attuale|corrente)\s+(?:di|per)\s+([a-zA-Z0-9.]+)",
        r"ticker\s+([a-zA-Z0-9.]+)"
    ]
    
    for pattern in realtime_patterns:
        match = re.search(pattern, message)
        if match:
            ticker = match.group(1).upper()
            return {"type": "realtime", "symbol": ticker}
    
    # Riconoscimento esplicito di ticker azionari
    ticker_match = re.search(r"\$([A-Za-z0-9.]+)", message)
    if ticker_match:
        ticker = ticker_match.group(1).upper()
        return {"type": "realtime", "symbol": ticker}

    if "cos'è" in message or "cosa vuol dire" in message:
        term = message.replace("cos'è", "").replace("cosa vuol dire", "").strip()
        return {"type": "definition", "term": term}

    if "cambio" in message:
        if "euro" in message and "dollaro" in message:
            return {"type": "currency", "base": "EUR", "target": "USD"}
        elif "dollaro" in message and "yen" in message:
            return {"type": "currency", "base": "USD", "target": "JPY"}

    tickers = {"apple": "AAPL", "fiat": "FCA.MI", "tesla": "TSLA"}
    for name, symbol in tickers.items():
        if fuzz.partial_ratio(name, message) > 80:
            return {"type": "stock", "symbol": symbol}

    return {"type": "unknown"}