# Imports

from utils.jsonImporting.jsonimport import readJSON
from utils.logger.logger import loggingF

# Main function

tranlsations = readJSON()

def cHello():

    loggingF(2, "Hello command has been executed")
    return tranlsations["command"]["hello"]