# Imports

import wikipedia
from utils.config.configR import configGet
from utils.jsonImporting.jsonimport import readJSON
from utils.logger.logger import loggingF
from utils.textToSpeech.textToSpeech import say

# Imports the translations

translations = readJSON()

# Configurate the language of wikipedia

loggingF(2, f"{configGet('wikipedia', 'languageW')} has been set as language for Wikipedia")
language = configGet('wikipedia', 'languageW')



wikipedia.set_lang(language)

def wikipediaSearch(data):
    
    if configGet("wikipedia", "enabled") == "True":
        data = data.replace("Wikipedia", "")

        try:
            
            result = wikipedia.summary(data, sentences = 4)
            loggingF(2, "Wikipedia command has been executed")
            say(translations["command"]["wikipedia"]["starting"])
            say(result)
        
        except wikipedia.exceptions.PageError:
            
            loggingF(4, "Wikipedia: page not found")
            say(translations["command"]["wikipedia"]["pageError"])
        
        except wikipedia.exceptions.HTTPTimeoutError:
            
            loggingF(4, "Wikipedia: HTTPTimeout error")  
            say(translations["command"]["wikipedia"]["HTTPTimeoutError"])
        
        except wikipedia.exceptions.DisambiguationError:
            
            loggingF(3, "Wikipedia: disambiguation error")
            say(translations["command"]["wikipedia"]["disambiguationError"])
    else:
        
        loggingF(2, "The function wikipedia is disabled")
        say(translations["command"]["disabled"])