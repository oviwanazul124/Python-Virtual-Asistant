import configparser

config = configparser.ConfigParser()

try:
    config.read('config.ini')
except configparser.Error:
    print("There was an error opening the configuration")

def configGet(sectionC, optionC):
    value = config.get(sectionC, optionC)
    return value