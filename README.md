# CodeClauseInternship_SpeechRecognition
# Voice Recorder and Speech-to-Text Assistant

This project is a simple Python-based voice assistant that records your voice, converts it to text, and then speaks the recognized text back to you.

## Features

- **Audio Recording:** Records audio from your microphone for a set duration.
- **Speech Recognition:** Converts recorded speech to text using Google's speech recognition API.
- **Text-to-Speech:** Reads the recognized text aloud using a text-to-speech engine.
- **No PyAudio Needed:** Uses `sounddevice`, `scipy`, and `wavio` for audio recording, making it compatible with Python 3.13+ and Windows.

## Requirements

Install the following Python packages before running the project:

```bash
pip install sounddevice scipy wavio speechrecognition pyttsx3 numpy
```

## How It Works

1. The script records your voice for 5 seconds and saves it as `output.wav`.
2. It processes the audio file and converts your speech to text.
3. The recognized text is printed and spoken back to you.

## Usage

Run the script from your terminal:

```bash
python main.py
```

## Files

- `main.py` — Main script for recording, recognizing, and speaking audio.

## Notes

- Make sure your microphone is connected and accessible.
- Internet connection is required for speech recognition (Google API).
- If you encounter errors about missing packages, install them using the command above.

## Example Output

```
Recording for 5 seconds...
Recording finished.
Recognizing...
You said: hello world
```
And the program will speak "hello world" aloud.

---

**Author:**  
Sakshi Agrahari
