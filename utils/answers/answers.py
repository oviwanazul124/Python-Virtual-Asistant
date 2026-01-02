# Imports

from utils.commands.openWeb.cOpenWeb import cOpenWeb
from utils.commands.shutdown.cShutdown import cShutdown
from utils.commands.openApp.cOpenApp import cOpenApp
from utils.commands.wikipediaSearch.wikipediaSearch import wikipediaSearch
from utils.jsonImporting.jsonimport import readJSON
from utils.textToSpeech.textToSpeech import say
from utils.logger.logger import loggingF

# Imports translations

loggingF(2, "The trasnlations from answer.py has been imported")
translations = readJSON()

# Main function

def answers(data):

    loggingF(2, f"The following data has been recived {data}")
    listening = True
    
    if "Hello" in data:

        loggingF(2, "Trying to execute the hello command")
        say(translations["command"]["hello"])

    # The second one, is to search in wikipedia anything

    elif "Wikipedia" in data:
        
        loggingF(2, "Trying to execute the wikipedia")
        value = wikipediaSearch(data)
        say(translations["command"]["wikipedia"]["starting"])
        say(value)

    # This commands opens webpages and apps, if inside 'data' is a '.com', will open a webpage, if not will run it as an app.

    elif "Open" in data:

        if ".com" in data:

            loggingF(2, "Trying to execute the cOpenWeb")
            value = cOpenWeb(data)
            say(value)
        else:

            loggingF(2, "Trying to execute the cOpenApp")
            value = cOpenApp(data)
            say(value)

    # This command exists the app

    elif "Exit" in data:

        loggingF(2, "Exiting...")
        exit(0)

    # This command shutdwon the system

    elif "Turn off" in data:

        loggingF(2, "Shutting Down the system...")
        say (translations["command"]["shutdown"]["starting"])
    

    # And this last command araises if he didn't understood what it said

    else:

        loggingF(3, "The speechRecognition couldn't understood what the user said")
        say(translations["sr"]["listeningError"])

    return listening
