from utils.jsonImporting.jsonimport import readJSON
from utils.logger.logger import loggingF
import webbrowser

translations = readJSON

def cOpenWeb(data):
    
    loggingF(2, "Open Web command has been executed")
    #! listening = true???
    data = data.replace("Open", "")
    data = data.replace(" ", "")
    data = "https://www." + data 
    try:
        webbrowser.open(data)
        return (translations["command"]["open"]["web"]["starting"] + data)
    except webbrowser.Error:
        return translations["command"]["open"]["web"]["error"]

