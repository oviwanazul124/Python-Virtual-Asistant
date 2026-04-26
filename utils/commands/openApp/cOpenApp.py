# Imports
from utils.config.configR import configGet
from utils.jsonImporting.jsonimport import readJSON
from utils.logger.logger import loggingF
from utils.readFiles.readFiles import readFiles
import subprocess

# Global Path

path = "null"

# Get translations

translations = readJSON()

# Main function

def cOpenApp(data):
    
    if configGet("openApp", "enabled") == "True":
        data = data.replace("Open", "")
        data = data.replace(" ", "")
        # Check if whitelist is active AND if the path is also active
        if configGet("openApp", "whitelist") == "True":
                
            if configGet ("openApp", "whilelistCustomPath") == "True":
                pass
        else:
            try:
                subprocess.run("start " + data + ".exe", shell=True)
                loggingF(2, "Open App command has been executed")
                return translations["command"]["open"]["app"]["starting"]
            except FileNotFoundError:
                loggingF(4, f"The {data} you have tried to open can't be accesed")
                return translations["command"]["open"]["app"]["fileNotFoundError"]
    else:
        loggingF(2, "The function openApp is disabled")
        return translations["command"]["disabled"]
