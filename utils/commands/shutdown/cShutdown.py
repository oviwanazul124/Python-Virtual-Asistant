# Imports

import platform
import subprocess
from utils.jsonImporting.jsonimport import readJSON
from utils.logger.logger import loggingF
from utils.config.configR import configGet
from utils.textToSpeech.textToSpeech import say

# Import translations

translations = readJSON()

# Check what platform the user is executing

rOS = platform.system()

# Main Function

def cShutdown():

    if configGet("shutdown", "enabled") == "True":
        loggingF(2, "Shutdown command has been executed")
        say(translations["command"]["shutdown"]["starting"])
        match rOS:
            case "Windows":
                subprocess.run("shutdown /p /f")
            case "Linux":
                subprocess.run("shutdown now")
            case "Darwin":
                subprocess.run("shutdown now")
            case _:
                loggingF(4 , "Shutdown command has encountered an error")
                say(translations["command"]["shutdown"]["error"])        
    else:
        loggingF(2, "The function shutdown is disabled")
        say (translations["command"]["disabled"])