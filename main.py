import speech_recognition as sr
from utils.jsonImporting.jsonimport import readJSON
from utils.speechRecognition.speechRecognition import recognize_speech
from utils.answers.answers import answers
from utils.textToSpeech.textToSpeech import runAndWait
# Get Translations

translations = readJSON()

# Start the Text-Speech engine and access to the API of Wikipedia

recognizer = sr.Recognizer()
microphone = sr.Microphone()

# The 'listening' variable, it used around the programm to check if the computer is listening or not

listening = True

# In this section of the code, if the variable listening is active will print: "Say something", after that will try to recognize what was said and will store it in a variable named
# data that will be used later on the commands.

while listening == True:
    print(translations["sr"]["listening"])
    data = recognize_speech(recognizer,microphone)
    listening = answers(data)
    runAndWait()
