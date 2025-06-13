const historyEl = document.getElementById('chat-box');

function appendMessage(text, type) {
    const div = document.createElement('div');
    div.className = `message ${type}`;
    div.textContent = text;
    historyEl.appendChild(div);
    historyEl.scrollTop = historyEl.scrollHeight;
}

// URL backend - fonctionne en local et sur Railway
const backendUrl = window.location.origin;

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

document.getElementById('send-button').addEventListener('click', send);

document.getElementById('message').addEventListener('keyup', (e) => {
    if (e.key === 'Enter') send();
});
