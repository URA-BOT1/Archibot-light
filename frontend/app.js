const historyEl = document.getElementById('chat-box'); // ou 'history' selon ton HTML

function appendMessage(text, type) {
    const div = document.createElement('div');
    div.className = `message ${type}`; // type = 'user' ou 'bot'
    div.textContent = text;
    historyEl.appendChild(div);
    historyEl.scrollTop = historyEl.scrollHeight;
}

const backendUrl =
    (typeof process !== 'undefined' && process.env && process.env.BACKEND_URL) ||
    window.BACKEND_URL ||
    '';

async function send() {
    const input = document.getElementById('message');
    const text = input.value.trim();
    if (!text) return;

    appendMessage(text, 'user');
    input.value = '';

    try {
        const res = await fetch(`${backendUrl}/chat`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: text })
        });
        const data = await res.json();
        appendMessage(data.reply || data.response || 'Réponse vide', 'bot');
    } catch (err) {
        appendMessage('Erreur : ' + err.message, 'bot');
    }
}

// Gestion du bouton d'envoi
document.getElementById('send-button').addEventListener('click', send);

// Envoi avec la touche Entrée
document.getElementById('message').addEventListener('keyup', (e) => {
    if (e.key === 'Enter') send();
});
