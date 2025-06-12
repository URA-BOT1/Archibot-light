function appendMessage(text, type) {
    const box = document.getElementById('chat-box');
    const div = document.createElement('div');
    div.className = `message ${type}`;
    div.textContent = text;
    box.appendChild(div);
    box.scrollTop = box.scrollHeight;
}

async function send() {
    const input = document.getElementById('message');
    const text = input.value.trim();
    if (!text) return;
    appendMessage(text, 'user');
    input.value = '';

    try {
        const res = await fetch('/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: text })
        });
        const data = await res.json();
        appendMessage(data.reply, 'bot');
    } catch (err) {
        appendMessage('Error sending message', 'bot');
    }
}

document.getElementById('send-btn').addEventListener('click', send);

document.getElementById('message').addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        send();
    }
});
