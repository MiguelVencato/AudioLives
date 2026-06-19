# from twitchio.ext import commands
# from threading import Thread

# from classifier import classify_message
# from templates import build_message
# from tts import speak

# from dotenv import load_dotenv
# import os

# load_dotenv()

# TWITCH_TOKEN = os.getenv("TWITCH_TOKEN")
# CHANNEL_NAME = os.getenv("TWITCH_CHANNEL")


# class SmartChatBot(commands.Bot):

#     def __init__(self):
#         super().__init__(
#             token=TWITCH_TOKEN,
#             prefix="!",
#             initial_channels=[CHANNEL_NAME]
#         )

#     async def event_ready(self):
#         print("================================")
#         print("Bot conectado à Twitch!")
#         print(f"Canal: {CHANNEL_NAME}")
#         print("================================")

#     async def event_message(self, message):

#         if message.echo:
#             return

#         user = message.author.name
#         content = message.content

#         print(f"\n{user}: {content}")

#         # Filtros simples para economizar tokens
#         if len(content.strip()) < 4:
#             return

#         if content.lower() in [
#             "kkk",
#             "kkkk",
#             "kkkkk",
#             "gg",
#             "opa",
#             "ok"
#         ]:
#             return

#         try:

#             category = classify_message(content)

#             final_message = build_message(
#                 user,
#                 content,
#                 category
#             )

#             print(f"Categoria: {category}")
#             print(f"TTS: {final_message}")

#             Thread(
#                 target=speak,
#                 args=(final_message,),
#                 daemon=True
#             ).start()

#         except Exception as e:
#             print(f"Erro: {e}")


# bot = SmartChatBot()
# bot.run()