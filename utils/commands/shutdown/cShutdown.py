# Imports

import platform
import subprocess
from utils.jsonImporting.jsonimport import readJSON
from utils.logger.logger import loggingF

# Import translations

translations = readJSON()

# Check what platform the user is executing

rOS = platform.system()

# Main Function

def cShutdown():

    loggingF(2, "Shutdown command has been executed")
    match rOS:
        case "Windows":
            subprocess.run("shutdown /p /f")
        case "Linux":
            subprocess.run("shutdown now")
        case "Darwin":
            subprocess.run("shutdown now")
        case _:

            loggingF(4 , "Shutdown command has encountered an error")
            return translations["command"]["shutdown"]["error"]        