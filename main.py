import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Use sounddevice as an alternative to PyAudio
try:
    import sounddevice as sd
    from scipy.io.wavfile import write
    import wavio
except ImportError:
    print("Please install sounddevice, scipy, and wavio: pip install sounddevice scipy wavio")
    exit(1)

import numpy as np

def record_audio(filename, duration=5, fs=44100):
    print(f"Recording for {duration} seconds...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    wavio.write(filename, audio, fs, sampwidth=2)
    print("Recording finished.")

def recognize_from_file(filename):
    with sr.AudioFile(filename) as source:
        audio = r.record(source)
        print("Recognizing...")
        MyText = r.recognize_google(audio)
        MyText = MyText.lower()
        print("You said: " + MyText)
        speak(MyText)

if __name__ == "__main__":
    filename = "output.wav"
    record_audio(filename, duration=5)
    recognize_from_file(filename)