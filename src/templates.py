templates = {
    "pergunta": "{user} perguntou: {message}",
    "alerta": "{user} alertou: {message}",
    "dica": "{user} sugeriu: {message}",
    "elogio": "{user} comentou: {message}",
    "comentario": "{user} disse: {message}"
}


def build_message(user, message, category):
    template = templates.get(
        category,
        "{user} disse: {message}"
    )

    return template.format(
        user=user,
        message=message
    )