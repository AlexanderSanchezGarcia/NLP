"""Practice 3° - 3° Partial"""
## January 08°, 2024
### ESCOM - IPN: *Natural Language Processing*
### Prof. Marco Antonio
### > Alexander Sanchez

from Voice.text_to_speech import speak
from Voice.speech_to_text import listen

speak("Hola, soy Aletza, tu asistente virtual.")

listened_text = listen()
listened_text = listened_text.strip()

if listened_text:
    speak("Dijiste")
    speak(listened_text)
else:
    speak("No logré entender lo que dijiste")

