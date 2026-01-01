import speech_recognition as sr
import pyttsx3
from utils.commands.wikipediaSearch.wikipediaSearch import wikipediaSearch
from utils.jsonImporting.jsonimport import readJSON
from utils.commands.openWeb.cOpenWeb import cOpenWeb
from utils.commands.shutdown.cShutdown import cShutdown
from utils.commands.openApp.cOpenApp import cOpenApp
# Get Translations

translations = readJSON()

# Start the Text-Speech engine and access to the API of Wikipedia

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)

# The 'listening' variable, it used around the programm to check if the computer is listening or not

listening = True

# To ease the code reading, we assign this two variables to the recognizer and the microphone.

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

# This part of the code, the data variable store info given for the user, with this we can check the type of command the user ask

def answer(data):

    listening = True
    
    # The first command is a 'Hello' command, is mostly used to check

    if "Hello" in data:
        engine.say(translations["command"]["hello"])

    # The second one, is to search in wikipedia anything

    elif "Wikipedia" in data:

        value = wikipediaSearch(data)
        engine.say(translations["command"]["wikipedia"]["starting"])
        engine.say(value)

    # This commands opens webpages and apps, if inside 'data' is a '.com', will open a webpage, if not will run it as an app.

    elif "Open" in data:

        if ".com" in data:
            value = cOpenWeb(data)
            engine.say(value)
        else:
            value = cOpenApp(data)
            engine.say(value)

    # This command exists the app

    elif "Exit" in data:
        exit(0)

    # This command shutdwon the system

    elif "Shutdown" or "Turn off" in data:
        engine.say (translations["command"]["shutdown"]["starting"])
        cShutdown()

    # And this last command araises if he didn't understood what it said

    else:
        engine.say(translations["sr"]["listeningError"])

    return listening

# In this section of the code, if the variable listening is active will print: "Say something", after that will try to recognize what was said and will store it in a variable named
# data that will be used later on the commands.

while listening == True:
    print(translations["sr"]["listening"])
    data = recognize_speech(recognizer,microphone)
    listening = answer(data)
    engine.runAndWait()
