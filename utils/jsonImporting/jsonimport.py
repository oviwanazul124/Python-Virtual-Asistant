from utils.config.configR import configGet
import json

def readJSON():
    try:
        with open("languages/" + configGet('baseConfig', 'language') + ".json", mode="r", encoding="utf-8") as read_file:
            translations = json.load(read_file)
            return translations
    except FileNotFoundError:
            print("I can't find the JSON")
            exit(1)
    except json.JSONDecodeError as e:
         print("There is an error in the JSON: ", e)
    except KeyError as e:
         print("Missing Key: ", e)