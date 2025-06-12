const historyEl = document.getElementById('history');

async function send() {
    const input = document.getElementById('message');
    const msg = input.value.trim();
    if (!msg) return;
    appendMessage('user', msg);
    input.value = '';

    try {
        const res = await fetch('/chat', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({message: msg})
        });
        const data = await res.json();
        appendMessage('bot', data.reply || data.response);
    } catch (err) {
        appendMessage('bot', 'Error: ' + err.message);
    }
}

function appendMessage(role, text) {
    const div = document.createElement('div');
    div.className = `message ${role}`;
    div.textContent = text;
    historyEl.appendChild(div);
    historyEl.scrollTop = historyEl.scrollHeight;
}

document.getElementById('send-button').addEventListener('click', send);
document.getElementById('message').addEventListener('keyup', (e) => {
    if (e.key === 'Enter') {
        send();
    }
});
