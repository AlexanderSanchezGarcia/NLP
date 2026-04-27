import sounddevice as sd
import soundfile as sf
import whisper

fs = 16000
seconds = 8

def listen():
    print("Escuchando...")
    audio = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()
    sf.write("Utils/audio.wav", audio, fs)

    model = whisper.load_model("base")
    result = model.transcribe("Utils/audio.wav", language="es")

    return result["text"]