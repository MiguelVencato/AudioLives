import queue
import threading
import asyncio
import re
import time  # Adicionado para dar um micro-tempo de respiro pro sistema operacional
import edge_tts
import pygame

speech_queue = queue.Queue()

# Inicializa o player de áudio do Pygame
pygame.mixer.init()

def clean_text(text: str) -> str:
    """Remove repetições exageradas para a IA não ficar presa na mesma letra."""
    return re.sub(r'(.)\1{2,}', r'\1\1', text)

async def generate_ai_voice(text, filename):
    voice = "pt-BR-AntonioNeural" 
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(filename)

def tts_worker():
    # Criamos dois arquivos fixos. O sistema vai revezar entre eles
    # para o Windows nunca bloquear a gravação da IA.
    files = ["tts_output_A.mp3", "tts_output_B.mp3"]
    file_index = 0
    
    while True:
        text = speech_queue.get()
        try:
            text_to_speak = clean_text(text)
        
            filename = files[file_index]
            file_index = (file_index + 1) % 2
            
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            time.sleep(0.1)

            asyncio.run(generate_ai_voice(text_to_speak, filename))
            pygame.mixer.music.load(filename)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
                
        except Exception as e:
            print(f"Erro no processamento do TTS: {e}")
        finally:
            speech_queue.task_done()
threading.Thread(target=tts_worker, daemon=True).start()

def speak(text):
    speech_queue.put(text)