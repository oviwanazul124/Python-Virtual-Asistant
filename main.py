import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import subprocess
from config import *

# Inicializar el engine para el Text-Speech y el acceso a la API de Wikipedia

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)
wikipedia.set_lang(mainLanguage)

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

# En esta sección del codigo la variable data, guarda la información propuesta por el usuario, mediante esto podremos saber que tipo de comando pide el usuario.

def answer(data):

    # El primer comando es un comando Hello, se podría denominar a estas alturas del desarrollo como un comando para comprobar si funciona.

    if "Hello" in data:
        listening = True
        engine.say("Hola, mi nombre es")

    # El segundo comando es una busqueda en Wikipedia de algún personaje.

    elif "Wikipedia" in data:
        listening = True
        
        # Esta linea remplaza todos los espacios que puedan a llegar a provocar problemas por "", facilitando la comprensión del programa.
        
        data = data.replace("Wikipedia", "")
        
        # En esta función prueba la conexión a Wikipedia, actualmente tiene configurados dos errores comúnes, el primer el cuál es un HTPPTtimeout y que la página no exista
        
        try:
            result = wikipedia.summary(data, sentences = 4)
            engine.say("Según wikipedia")
            engine.say(result)
        except wikipedia.exceptions.PageError:
            engine.say("No existe esa pagina en Wikipedia")
        except wikipedia.exceptions.HTTPTimeoutError:
            engine.say("Hubo un error conectandose a Wikipedia")
        except wikipedia.exceptions.DisambiguationError:
            engine.say("Existen demasiadas páginas con el mismo nombre, porfavor especifica")

    # En este otro comando, se encarga de abrir páginas / aplicaciones, si dentro de 'data' existe un ".com", correra el código de abrir páginas si no correra la app.

    elif "Open" in data:

        if ".com" in data:

            listening = True
            data = data.replace("Open", "")
            data = data.replace(" ", "")
            data = "https://www." + data 


            # Esto se encarga de controlar los errores que puede llegar a tener el comando, los errores soportados son únicamente un error predeterminado del navegador.

            engine.say("Se ha abierto" + data)
            try:
                webbrowser.open(data)
            except webbrowser.Error:
                engine.say("Hubo un error con el navegador, intentelo más tarde")
        
        # Por otro lado este el código que se encarga del soporte de abrir aplicaciones.

        else:
            listening = True
            data = data.replace("Open", "")
            data = data.replace(" ", "")
            
            # Esta parte del código se encarga de controlar los errores producidos por este comando 

            try:
                subprocess.run("start " + data + ".exe", shell=True)
            except FileNotFoundError:
                engine.say("No se ha encontrado la aplicación especificada")
   

    # Este comando se encarga de cerrar la aplicación, y cerrar todos los script relacionados a ellos.

    elif "Exit" in data:
        exit()

    # Este comando se encarga de cerrar el sistema sin aviso de apagado de las aplicaciones.

    elif "Shutdown" in data:
        engine.say ("Se ha apagado el sistema")
        subprocess.run("shutdown /p /f")
        pass


    # Este comando se encarga de obtener la hora del día y del sistema y decirsela al usuario.
    #! Este sección del código no esta terminada, es solo un placeholder

    elif "time" in data:
        pass

    # Este comando es usado para si no se reconoce ningúno de los siguientes comandos

    else:
        listening = True
        engine.say("Creo que no lo he entendido, ¿Puedes repetir?")

    return listening

# En esta sección del codigo, si la variable de escucha se encuentra activa printeara: "Say somenthing:" posteriormente reconocera lo dicho y lo guardara en una variable llamada
# data esta se usa posteriormente para poder visualizar cuales de los comandos disponibles han sidos dichos por el usuario.

while listening == True:
    print("Say something: ")
    data = recognize_speech(recognizer,microphone)
    listening = answer(data)
    engine.runAndWait()

