from openai import OpenAI
from config import OPENROUTER_API_KEY, MODEL_NAME

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY
)


def classify_message(message: str) -> str:
    prompt = f"""
Classifique a mensagem em apenas UMA categoria.

Categorias possíveis:
- pergunta
- alerta
- dica
- elogio
- comentario

Responda SOMENTE com o nome da categoria.

Mensagem:
{message}
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content.strip().lower()