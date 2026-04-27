from Voice.speech_to_text import listen
from Voice.text_to_speech import speak

def generate_story():
    speak("Dime un objeto")
    objeto = listen()

    speak("Dime una acción")
    accion = listen()

    speak("Dime un país")
    pais = listen()

    speak("Dime un año")
    año = listen()

    historia = (
        f"En el año {año}, en {pais}, "
        f"un {objeto} decidió {accion}. "
        "Lo que ocurrió después cambió la historia para siempre."
    )

    speak(historia)