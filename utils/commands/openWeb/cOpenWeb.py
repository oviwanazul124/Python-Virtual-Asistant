# Imports

from utils.config.configR import configGet
from utils.jsonImporting.jsonimport import readJSON
from utils.logger.logger import loggingF
from utils.textToSpeech.textToSpeech import say
import webbrowser

# Imports translations

translations = readJSON()

# Main functions

def cOpenWeb(data):
    
    if configGet("openWeb", "enabled") == "True":
        data = data.replace("Open", "")
        data = data.replace(" ", "")
        data = "https://www." + data 

        try:
            webbrowser.open(data)
            loggingF(2, "Open Web command has been executed")
            say(translations["command"]["open"]["web"]["starting"] + data)
        except webbrowser.Error:
            loggingF(4, f"There was an error opening the {data} webpage")
            say(translations["command"]["open"]["web"]["error"])
    else:
        loggingF(2, "The function openWeb is disabled")
        say(translations["command"]["disabled"])
