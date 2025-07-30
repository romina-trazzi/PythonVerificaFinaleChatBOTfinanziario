import yfinance as yf

# Parsing messaggi utente
from services.chat_parser import interpret_message

# Servizi finanziari
from services.finance_data import get_price
from services.currency_data import get_exchange
from services.glossary import get_definition
from services.realtime_finance_data import get_realtime_data  # Nuovo import

# Grafici e PDF
from services.chart_generator import generate_chart
from services.pdf_generator import generate_pdf_report

# Fallback: chiamata a LLM se il messaggio è vago o fuori scope
from services.openai_chat import ask_llm


def handle_user_message(message):
    intent = interpret_message(message)

    # Nuovo tipo di intent per dati in tempo reale
    if intent["type"] == "realtime":
        data = get_realtime_data(intent["symbol"])
        if data["success"]:
            return f"📊 Dati in tempo reale per {data['name']} ({intent['symbol']}):\n" \
                   f"Prezzo: {data['price']} {data['currency']}\n" \
                   f"Variazione: {data['change']}\n" \
                   f"Fonte: {data['source']}"
        else:
            return f"❌ Non è stato possibile ottenere dati in tempo reale per {intent['symbol']}: {data['error']}"

    elif intent["type"] == "stock":
        return f"Il prezzo corrente di {intent['symbol']} è {get_price(intent['symbol'])} USD."

    elif intent["type"] == "currency":
        rate = get_exchange(intent["base"], intent["target"])
        return f"Il cambio attuale {intent['base']}/{intent['target']} è {rate}."

    elif intent["type"] == "definition":
        definition = get_definition(intent["term"])
        if definition == "Definizione non trovata.":
            return ask_llm(f"Spiegami in modo semplice: {intent['term']}")
        return definition

    elif intent["type"] == "graph":
        chart_path = generate_chart(intent["symbol"])
        return f"Grafico generato per {intent['symbol']}. Lo trovi in: {chart_path}"

    elif intent["type"] == "report":
        df = yf.Ticker(intent["symbol"]).history(period="6mo")
        chart_path = generate_chart(intent["symbol"])
        pdf_path = generate_pdf_report(intent["symbol"], chart_path, df.describe().to_html())
        return f"Report PDF creato per {intent['symbol']}. Percorso: {pdf_path}"

    # Fallback: se non riconosciuto, chiedi al modello
    else:
        return ask_llm(message)