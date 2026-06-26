import pyttsx3
import queue
import threading

engine = pyttsx3.init()
speech_queue = queue.Queue()

def tts_worker():
    while True:
        text = speech_queue.get()
        try:
            engine.say(text)
            engine.runAndWait()
        finally:
            speech_queue.task_done()

threading.Thread(target=tts_worker, daemon=True).start()

def speak(text):
    speech_queue.put(text)