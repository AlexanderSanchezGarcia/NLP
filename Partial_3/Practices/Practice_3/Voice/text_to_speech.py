import pyttsx3

# Init pyttsx3 engine
engine = pyttsx3.init()

# Voice settings
engine.setProperty("rate", 165)
engine.setProperty("volume", 1.0)

es_voice = "com.apple.voice.compact.es-MX.Paulina"
en_voice = "com.apple.voice.compact.en-US.Samantha"

def set_voice(engine, language="en"):
    if language == "es":
        engine.setProperty("voice", es_voice)
    else:
        engine.setProperty("voice", en_voice)

set_voice(engine, language="es")

def speak(text):
    print("Aletza:", text)
    engine.say(text)
    engine.runAndWait()