from flask import Flask, request, render_template_string
from priority import calculate_priority, should_read
from tts import speak
from classifier import classify_message
from templates import build_message

app = Flask(__name__)

chat_history = []

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Leitor de Chat Inteligente</title>
    <style>
        body {
            background: #0e0e10;
            color: white;
            font-family: Arial, sans-serif;
            max-width: 1000px;
            margin: auto;
            padding: 20px;
        }
        h1 {
            text-align: center;
            color: #9146ff;
        }
        .chat {
            border: 1px solid #444;
            border-radius: 8px;
            height: 500px;
            overflow-y: auto;
            padding: 15px;
            margin-bottom: 20px;
            background: #18181b;
        }
        .message {
            margin-bottom: 15px;
            padding: 15px;
            background: #26262c;
            border-radius: 8px;
        }
        .username {
            color: #9146ff;
            font-weight: bold;
            font-size: 16px;
        }
        .category {
            color: #00d084;
            font-weight: bold;
        }
        .tts {
            color: #ffd166;
        }
        input, button {
            width: 100%;
            padding: 12px;
            margin-bottom: 10px;
            border-radius: 6px;
            border: none;
            box-sizing: border-box;
        }
        button {
            background: #9146ff;
            color: white;
            font-weight: bold;
            cursor: pointer;
        }
        button:hover {
            background: #7d39e0;
        }
    </style>
</head>
<body>

    <h1>🎮 Leitor de Chat Inteligente</h1>

    <div class="chat">
        {% for msg in history %}
        <div class="message">
            <div class="username">{{ msg.user }}</div>

            <p><strong>Mensagem:</strong><br>{{ msg.original }}</p>

            <p><strong>Score:</strong><br>{{ msg.score }}</p>

            <p>
                <strong>Categoria:</strong><br>
                <span class="category">{{ msg.category }}</span>
            </p>

            <p>
                <strong>TTS:</strong><br>
                <span class="tts">{{ msg.final }}</span>
            </p>
        </div>
        {% endfor %}
    </div>

    <form method="POST">
        <input type="text" name="user" placeholder="Nome do usuário" required>
        <input type="text" name="message" placeholder="Digite uma mensagem..." required>
        <button type="submit">Enviar Mensagem</button>
    </form>

    <script>
        const chat = document.querySelector(".chat");
        chat.scrollTop = chat.scrollHeight;
    </script>

</body>
</html>
"""
@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":
        user = request.form["user"]
        message = request.form["message"]
        score = calculate_priority(message)
        category = classify_message(message)
        if category in ["odio", "spam"]:
            final_message = "Mensagem removida pelo sistema de moderação."

        else:
            if should_read(message):
                final_message = build_message(user, message, category)
                speak(final_message)
            else:
                final_message = "Mensagem ignorada por baixa prioridade."
        chat_history.append({
            "user": user,
            "original": message,
            "score": score,
            "category": category,
            "final": final_message
        })
    return render_template_string(HTML, history=chat_history)
if __name__ == "__main__":
    app.run(debug=True)