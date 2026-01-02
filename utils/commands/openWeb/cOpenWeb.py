# Imports

from utils.jsonImporting.jsonimport import readJSON
from utils.logger.logger import loggingF
import webbrowser

# Imports translations

translations = readJSON()

# Main functions

def cOpenWeb(data):

    data = data.replace("Open", "")
    data = data.replace(" ", "")
    data = "https://www." + data 

    try:
        webbrowser.open(data)
        loggingF(2, "Open Web command has been executed")
        return (translations["command"]["open"]["web"]["starting"] + data)
    except webbrowser.Error:
        loggingF(4, f"There was an error opening the {data} webpage")
        return translations["command"]["open"]["web"]["error"]

