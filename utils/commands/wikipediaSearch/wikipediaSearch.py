import wikipedia
from utils.config.configR import configGet
from utils.jsonImporting.jsonimport import readJSON
from utils.logger.logger import loggingF

translations = readJSON()

language = configGet('wikipedia', 'languageW')

wikipedia.set_lang(language)

def wikipediaSearch(data):
    
    loggingF(2, "Wikipedia command has been executed")
    data = data.replace("Wikipedia", "")

    try:
        result = wikipedia.summary(data, sentences = 4)
        return result
    except wikipedia.exceptions.PageError:
        return translations["command"]["wikipedia"]["pageError"]
    except wikipedia.exceptions.HTTPTimeoutError:
        return translations["command"]["wikipedia"]["HTTPTimeoutError"]
    except wikipedia.exceptions.DisambiguationError:
        return translations["command"]["wikipedia"]["disambiguationError"]
