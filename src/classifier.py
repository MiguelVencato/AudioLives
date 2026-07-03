import time
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
- pergunta (usuário tirando dúvidas sobre o jogo, streamer ou puxando assunto com perguntas de interação)
- alerta (informação útil sobre o jogo ou a transmissão)
- dica (sugestão de gameplay de forma respeitosa)
- elogio (mensagem positiva, apoio ou comemoração direcionada explicitamente ao streamer ou à live)
- comentario (mensagens neutras, conversas gerais, auto-elogios e reações comuns da internet)
- spam (mensagens sem sentido, flood, links suspeitos ou repetições excessivas)
- odio (conteúdo ofensivo, assédio, preconceito, toxicidade direcionada ou agressividade pesada)

Diretrizes Críticas para Casos Complexos:
1. Palavrões e Gírias: Expressões como "porra", "caralho", "pqp" usadas para expressar surpresa, empolgação ou frustração com o JOGO devem ser classificadas como COMENTÁRIO ou ELOGIO (ex: "caralho que jogada foda" -> elogio).
2. Mensagens "Pouco Ofensivas" / Passivo-Agressivas: Mensagens com tom de deboche disfarçado, cobranças ácidas, ironia depreciativa ou negatividade gratuita direcionada ao streamer ou a outros usuários (ex: "joga muito... sqn", "essa live já foi melhor", "que build burra") devem ser classificadas diretamente como ODIO. Se a intenção for diminuir alguém, mesmo que sem palavrão, mude para ODIO.
3. Mensagens Secas/Sem Sentimento: Se a mensagem for apenas uma crítica seca ao jogo (ex: "esse jogo tá chato hoje"), classifique como COMENTÁRIO. Se for uma crítica destrutiva à pessoa (ex: "você tá chato hoje"), classifique como ODIO.
4. Cumprimentos e Perguntas de Interação: Mensagens que usam ponto de interrogação (?) ou que claramente esperam uma resposta/atualização do streamer, incluindo saudações interativas (ex: "Oi tudo bem por ai?", "beleza?", "vai jogar até que horas?") devem ser obrigatoriamente classificadas como PERGUNTA.
5. Auto-elogios e Ego: Se o usuário estiver elogiando a si mesmo (ex: "Eu sou maravilhosa", "joguei muito agora"), classifique como COMENTÁRIO. A categoria ELOGIO deve ser usada estritamente para quando o elogio for para o streamer, para a live ou para a jogada do streamer.

Formato de Resposta:
Responda RIGOROSAMENTE apenas com o nome da categoria escolhida, sem pontuação ou texto adicional.

Mensagem:
{message}
"""

    max_tentativas = 3
    
    for tentativa in range(1, max_tentativas + 1):
        try:
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

        except Exception as e:
            print(f"⚠️ [Tentativa {tentativa}/{max_tentativas}] Servidor do OpenRouter instável ou ocupado. Erro: {e}")
            if tentativa < max_tentativas:
                time.sleep(1.5)
            else:
                print("🚨 [FALHA TOTAL] OpenRouter indisponível após 3 tentativas. Ignorando e assumindo padrão 'comentario'.")
                return "comentario"