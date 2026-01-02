# Import

from utils.config.configR import configGet
from utils.logger.logger import loggingF
import json

# Main fuction

def readJSON():
    try:
        with open("languages/" + configGet('baseConfig', 'language') + ".json", mode="r", encoding="utf-8") as read_file:
            translations = json.load(read_file)
            return translations
    except FileNotFoundError:
            print("There was an error please check the log for more info")
            loggingF(4, f"The {configGet('baseConfig', 'language')}.json has been not found")
            exit(1)
    except json.JSONDecodeError as e:
         
         print("There was an error please check the log for more info")
         loggingF(4, f"There was a syntax error on the JSON: {e}")
         exit(1)
    except KeyError as e:
         print("There was an error please check the log for more info")
         loggingF(4, f"The key reference {e} dosen't exists")
         exit(1)