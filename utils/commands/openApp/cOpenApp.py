from utils.jsonImporting.jsonimport import readJSON
from utils.logger.logger import loggingF
import subprocess

# Get translations

translations = readJSON()

# Main function

def cOpenApp():
    
    loggingF(2, "Open App command has been executed")
    data = data.replace("Open", "")
    data = data.replace(" ", "")

    try:
        subprocess.run("start " + data + ".exe", shell=True)
        return translations["command"]["open"]["app"]["starting"]
    except FileNotFoundError:
        return translations["command"]["open"]["app"]["fileNotFoundError"]
pass
