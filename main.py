import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
from subprocess import call


# Inicializar el engine para el Text-Speech y el acceso a la API de Wikipedia

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)
wikipedia.set_lang("es")

# La variable 'listening', se utiliza a lo largo del programa para indicar si el ordenador esta escuchando o no esta escuchando

listening = True

# Aqui, para facilitar en codigo, se le dan dos variables a las funciones principales
# del uso del reconocedor y microfono base del sistema

recognizer = sr.Recognizer()
microphone = sr.Microphone()

def recognize_speech(recognizer, microphone):
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        speech = recognizer.recognize_whisper(audio, translate = True)
        print("You said: ", speech)
    except sr.RequestError:
        print("There isn't an WhisperAI model installed")
    except sr.UnknownValueError:
        print("Could not understand what you said")
    return speech

def answer(data):
    if "Hello" in data:
        listening = True
        engine.say("Hola, mi nombre es")

    elif "Wikipedia" in data:
        listening = True
        data = data.replace("Wikipedia", "")
        try:
            result = wikipedia.summary(data, sentences = 4)
            engine.say("Según wikipedia")
            engine.say(result)
        except wikipedia.exceptions.PageError:
            engine.say("No existe esa pagina en Wikipedia")
        except wikipedia.exceptions.HTTPTimeoutError:
            engine.say("Hubo un error conectandose a Wikipedia")   

    elif "Open" in data:

        if ".com" in data:

            listening = True
            data = data.replace("Open", "")
            data = data.replace(" ", "")
            data = "https://www." + data 

            engine.say("Se ha abierto" + data)
            try:
                webbrowser.open(data)
            except webbrowser.Error:
                engine.say("Hubo un error con el navegador, intentelo más tarde")

        else:
            listening = True
            data = data.replace("Open", "")
            data = data.replace(" ", "")
            
            try:
                call([data + ".exe"])
            except FileNotFoundError:
                engine.say("No se ha encontrado la aplicación especificada")
   
    elif "Exit" in data:
        exit()

    else:
        listening = True
        engine.say("Creo que no lo he entendido, ¿Puedes repetir?")

    return listening

while listening == True:
    print("Say something: ")
    data = recognize_speech(recognizer,microphone)
    listening = answer(data)
    engine.runAndWait()

