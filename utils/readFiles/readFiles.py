# Imports
from utils.logger.logger import loggingF

def readFiles(type, path, word):

    loggingF(1, f"readFiles has been called with {type} with the path: '{path}' and with the word '{word}'")

# Main logic for reading files
    with open(path, "r") as file:
        for line in file:
            if word in line:
                output = line

# Tinkering with outputs if necessary
    match type:
        # This case is dedicated for the cOpenApp Whitelist
        case 1:
            loggingF(1, f"readFiles ended without any problem with type {type}")
            output = output.replace(word, "")
            output = output.replace("=", "")
            return output
        case _:
            loggingF(3, "There wasn't any type specified in readFiles, could it be intentional")
            return output