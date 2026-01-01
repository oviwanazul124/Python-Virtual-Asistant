import platform
import subprocess
from utils.jsonImporting.jsonimport import readJSON
from utils.logger.logger import loggingF

translations = readJSON()

rOS = platform.system()

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
            return translations["command"]["shutdown"]["error"]        