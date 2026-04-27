import speech_recognition as sr

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language="es-MX")
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        return "I did not understand that."