// Riferimenti agli elementi DOM
// Riferimenti agli elementi DOM

const form = document.getElementById("chat-form");
const input = document.getElementById("chat-input");
const chatBox = document.getElementById("chat-box");
const loading = document.getElementById("loading");

// Event listener per il form di chat
form.addEventListener("submit", function(e) {
    e.preventDefault();
    const message = input.value.trim();
    if (!message) return;
    
    // Aggiungi il messaggio dell'utente
    appendMessage("user", message);
    input.value = "";
    input.disabled = true;
    loading.classList.remove("d-none");
    document.body.style.cursor = "wait";

    // Invia la richiesta al server
    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message })
    })
    .then(res => res.json())
    .then(data => {
        appendMessage("bot", data.response);
    })
    .catch(err => {
        appendMessage("bot", "Si è verificato un errore nella richiesta.");
    })
    .finally(() => {
        input.disabled = false;
        loading.classList.add("d-none");
        document.body.style.cursor = "default";
    });
});

// Funzione per aggiungere messaggi alla chat
function appendMessage(sender, text) {
    const msgDiv = document.createElement("div");
    msgDiv.className = "message " + sender;

    const bubble = document.createElement("div");
    bubble.className = "text";
    bubble.innerHTML = text;

    msgDiv.appendChild(bubble);
    chatBox.appendChild(msgDiv);

    // Se c'è un percorso immagine, lo mostriamo come immagine (es. output/charts/abc.png)
    const imageRegex = /(output\/charts\/\S+\.png)/;
    const match = text.match(imageRegex);
    if (match) {
        const img = document.createElement("img");
        img.src = "/" + match[1];  // Flask serve statico
        img.className = "image-response";
        chatBox.appendChild(img);
    }

    chatBox.scrollTop = chatBox.scrollHeight;
}