
import edge_tts
import asyncio
import pygame
import tempfile
import os

async def speak(text):
   temp_file = tempfile.mktemp(suffix=".mp3")
   communicate = edge_tts.Communicate(text, "en-US-AriaNeural")
   await communicate.save(temp_file)
   pygame.mixer.init()
   pygame.mixer.music.load(temp_file)
   pygame.mixer.music.play()
   while pygame.mixer.music.get_busy():
    await asyncio.sleep(0.1)
   pygame.mixer.music.unload()
   os.remove(temp_file)
