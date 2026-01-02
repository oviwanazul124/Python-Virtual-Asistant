# Imports

from utils.jsonImporting.jsonimport import readJSON
from utils.logger.logger import loggingF
import subprocess

# Get translations

translations = readJSON()

# Main function

def cOpenApp(data):
    
    data = data.replace("Open", "")
    data = data.replace(" ", "")

    try:
        subprocess.run("start " + data + ".exe", shell=True)
        loggingF(2, "Open App command has been executed")
        return translations["command"]["open"]["app"]["starting"]
    except FileNotFoundError:
        loggingF(4, f"The {data} you have tried to open can't be accesed")
        return translations["command"]["open"]["app"]["fileNotFoundError"]
pass
