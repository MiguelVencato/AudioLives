from openai import OpenAI
from config import OPENROUTER_API_KEY, MODEL_NAME

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY
)


def classify_message(message: str) -> str:
    prompt = f"""
Você é um moderador de chat de live de jogos altamente criterioso e contextual.
Sua tarefa é classificar a mensagem do usuário em uma única categoria e determinar se ela viola as diretrizes de convivência da live.

Categorias permitidas:
- pergunta (usuário tirando dúvidas sobre o jogo ou streamer)
- alerta (informação útil sobre o jogo ou a transmissão)
- dica (sugestão de gameplay de forma respeitosa)
- elogio (mensagem positiva, apoio ou comemoração)
- comentario (mensagens neutras, conversas gerais e reações comuns da internet)
- spam (mensagens sem sentido, flood, links suspeitos ou repetições excessivas)
- odio (conteúdo ofensivo, assédio, preconceito, toxicidade direcionada ou agressividade pesada)

Diretrizes Críticas para Casos Complexos:
1. Palavrões e Gírias: Expressões como "porra", "caralho", "pqp" usadas para expressar surpresa, empolgação ou frustração com o JOGO devem ser classificadas como COMENTÁRIO ou ELOGIO (ex: "caralho que jogada foda" -> elogio).
2. Mensagens "Pouco Ofensivas" / Passivo-Agressivas: Mensagens com tom de deboche disfarçado, cobranças ácidas, ironia depreciativa ou negatividade gratuita direcionada ao streamer ou a outros usuários (ex: "joga muito... sqn", "essa live já foi melhor", "que build burra") devem ser classificadas diretamente como ODIO. Se a intenção for diminuir alguém, mesmo que sem palavrão, mude para ODIO.
3. Mensagens Secas/Sem Sentimento: Se a mensagem for apenas uma crítica seca ao jogo (ex: "esse jogo tá chato hoje"), classifique como COMENTÁRIO. Se for uma crítica destrutiva à pessoa (ex: "você tá chato hoje"), classifique como ODIO.

Formato de Resposta:
Responda RIGOROSAMENTE apenas com o nome da categoria escolhida, sem pontuação ou texto adicional.

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