# 💬 Chatbot Finanziaria Web 📊

Progetto d’esame – ITS ICT PiemonteTitolo: Chatbot finanziaria web con scraping/API di dati di mercatoDurata 
Autori: Ashna Kaur, Mattia Martinelli, Elia Sollazzo, Glaglanie Tchissambou, Romina Trazzi

📌 Obiettivo

Realizzare un'applicazione interamente in Python che consenta all’utente di:

- Interagire con una chatbot finanziaria via web
- Ottenere dati di mercato in tempo reale (prezzi, variazioni, ticker, definizioni)
- Visualizzare le risposte in modo chiaro (inclusi grafici o report PDF)

🧐 Funzionalità

### ✅ Parte 1 – Chatbot Finanziaria

Risponde a domande frequenti come:

1. “Cos'è un ETF?”
2. “Cosa vuol dire P/E ratio?”

Implementata tramite:

- Glossario locale (dizionario Python)
- Modello LLM per risposte avanzate

### ✅ Parte 2 – Dati Reali via API o Scraping 

Scraping Google Finance (con requests + BeautifulSoup)

Integrazione con API gratuite (es. AlphaVantage, OpenRouter, yfinance)

Ricerca di:

- Prezzo azione (es. AAPL, TSLA)

Variazione giornaliera

Nome completo del titolo

✅ Parte 3 – Web App Flask 

Interfaccia web semplice e responsive con visualizzazione chatbot + dati finanziari, messaggi utente/bot


🚀 Come eseguire il progetto

1. Clona il repository

git clone https://https://github.com/romina-trazzi/PythonVerificaFinaleChatBOTfinanziario
cd PythonVerificaFinaleChatBOTfinanziario

2. Installa le dipendenze

pip install -r requirements.txt

3. Crea un file .env con le tue API Key
OPENROUTER_API_KEY=sk-...

4. Avvia il server

python app.py

Apri il browser su http://localhost:5000





## 📚 Screenshot
![static/img/chartpart2.png](https://github.com/romina-trazzi/PythonVerificaFinaleChatBOTfinanziario/blob/master/static/img/finale.JPG)
![static/img/chartpart1.png](https://github.com/romina-trazzi/PythonVerificaFinaleChatBOTfinanziario/blob/master/static/img/finale2.JPG)



## 📁 Struttura del progetto

.
├── app.py
├── api/
│   └── api_routes.py
├── controller/
│   └── chat_controller.py
├── services/
│   ├── openai_chat.py
│   ├── glossary.py
│   ├── chart_generator.py
│   ├── finance_data.py
│   └── ...
├── templates/
│   └── index.html
├── static/
│   ├── css/
│   └── output/charts/
├── .env
└── README.md

Dopo aver implementato queste modifiche, potrai utilizzare il chatbot per ottenere dati in tempo reale in questi modi:

1. "Dammi i dati in tempo reale per AAPL"
2. "Qual è il prezzo attuale di TSLA?"
3. "Ticker MSFT"
4. "$AMZN" -usando il simbolo $ seguito dal ticker

✅ Conclusione

Questo progetto dimostra come Python possa essere usato per costruire un'applicazione web interattiva, integrando intelligenza artificiale, scraping web e finanza. Un ottimo esempio di full stack Python development per dati reali.

#### 👨‍🎓 Realizzato per l'esame finale

Corso Python & Machine Learning – ITS ICT Piemonte
