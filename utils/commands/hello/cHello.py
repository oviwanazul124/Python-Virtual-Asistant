# Imports

from utils.jsonImporting.jsonimport import readJSON
from utils.logger.logger import loggingF
from utils.config.configR import configGet

# Main function

translations = readJSON()

def HelloCommand():
        
    if configGet("hello", "enabled") == "True":
        loggingF(2, "Hello command has been executed")
        return translations["command"]["hello"]
    else:
        loggingF(2, "The function hello is disabled")
        return translations["command"]["disabled"]