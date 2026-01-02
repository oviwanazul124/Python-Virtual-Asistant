import speech_recognition as sr
from utils.jsonImporting.jsonimport import readJSON

translations = readJSON()

recognizer = sr.Recognizer()
microphone = sr.Microphone()

def recognize_speech(recognizer, microphone):
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        speech = recognizer.recognize_whisper(audio, model="medium",task="translate")
        print(translations["sr"]["said"], speech)
    except sr.RequestError:
        print(translations["sr"]["resquestError"])
    except sr.UnknownValueError:
        print(translations["sr"]["unknownValueError"])
    return speech
