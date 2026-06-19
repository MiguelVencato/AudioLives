from openai import OpenAI
from config import OPENROUTER_API_KEY, MODEL_NAME

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY
)


def classify_message(message: str) -> str:
    prompt = f"""
Você é um classificador de mensagens de chat de live de jogos.
Classifique a mensagem em APENAS UMA categoria:
Categorias:
- pergunta (usuário perguntando algo)
- alerta (informação útil do jogo)
- dica (sugestão de gameplay)
- elogio (mensagem positiva)
- comentario (neutro)
- spam (mensagem sem sentido ou repetitiva)
- odio (conteúdo ofensivo, discurso de ódio ou agressivo pesado)
Regras importantes:
- Palavrões leves NÃO são odio se não serem dirigidos a alguém ou não forem agressivos (ex: porra, que foda, caralho que legal entre outros) pode classificar como comentario nesse caso
- Só marque como odio se for realmente ofensivo, agressivo ou discriminatório
- Responda SOMENTE com uma palavra da lista
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