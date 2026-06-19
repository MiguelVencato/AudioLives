templates = {
    # Templates falados das categorias
    "pergunta": "{user} perguntou: {message}",
    "alerta": "{user} alertou: {message}",
    "dica": "{user} sugeriu: {message}",
    "elogio": "{user} elogiou: {message}",
    "comentario": "{user} comentou: {message}",
    # Templates Ignorados
    "spam": "{user} enviou uma mensagem ignorada pelo sistema.",
    "odio": "{user} teve a mensagem removida por moderação."
}


def build_message(user, message, category):
    template = templates.get(
        category,
        "{user} disse: {message}"
    )
    if category in ["spam", "odio"]:
        return template.format(user=user, message="")

    return template.format(
        user=user,
        message=message
    )