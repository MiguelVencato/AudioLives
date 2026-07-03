import os
from twitchio.ext import commands
from dotenv import load_dotenv
from classifier import classify_message
from priority import calculate_priority, should_read
from templates import build_message
from tts import speak

load_dotenv()

TWITCH_TOKEN = os.getenv("TWITCH_TOKEN")
CHANNEL_NAME = os.getenv("CHANNEL_NAME")

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(
            token=TWITCH_TOKEN, 
            prefix='!', 
            initial_channels=[CHANNEL_NAME]
        )

    async def event_ready(self):
        print(f'\n Sistema de TTS Rodando! Canal: {CHANNEL_NAME}')
        print("Aguardando mensagens DESTACADAS (100 pontos)...\n")

    async def event_message(self, message):
        if message.echo:
            return
        msg_id = message.tags.get('msg-id')
        if msg_id != 'highlighted-message':
            return
        user = message.author.name
        text = message.content

        print(f"[RESGATE POR PONTOS] {user} destacou a mensagem: {text}")
        score = calculate_priority(text)
        if not should_read(text):
            print(f" Mensagem de {user} ignorada por ser curta demais.\n")
            return

        category = classify_message(text)
        print(f"📊 Categoria: {category} | Score: {score}")

        if category in ["odio", "spam"]:
            print(f"🛡️ [MODERAÇÃO] Mensagem de {user} bloqueada por {category.upper()}.\n")
            return
        final_message = build_message(user, text, category)
        print(f"🔊 Falando com voz de IA: \"{final_message}\"\n")
        speak(final_message)

        await self.handle_commands(message)

if __name__ == "__main__":
    bot = Bot()
    bot.run()