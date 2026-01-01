import logging
from pathlib import Path
from datetime import datetime

def projectRoot() -> Path:
    return Path(__file__).resolve().parents[2]

def getLogsDir() -> Path:
    logsDir = projectRoot() / "logs"
    return logsDir

def logCreate() -> Path:

    time = datetime.now().strftime("Y-%m-%d_%H-%M-%S")
    logFile = getLogsDir() / f"{time}.log"
    with logFile.open("w", encoding="utf-8") as file:
        file.write(f"{time} has log created succesfully")
    return logFile


logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',filename=f"{logCreate()}", encoding='utf-8', level=logging.DEBUG)

def loggingF(type, string):

    match type:
        case 1:
            logger.debug(string)
        case 2:
            logger.info(string)
        case 3:
            logger.warning(string)
        case 4:
            logger.error(string)
        case _:
            logger.error("Logger is not working")
