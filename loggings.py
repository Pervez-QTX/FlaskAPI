import logging
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

# logging.basicConfig(level=logging.INFO, format="%(asctime)s::%(levelname)s::%(message)s", filename="test.log")

# logging.info("Hey")
# logging.critical("It is critical log")

logger = logging.getLogger("my_logger")
logger.setLevel(logging.INFO)


consolehandler = logging.StreamHandler()
consoleformatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", datefmt = "%Y-%m-%d %H:%M:%S")
consolehandler.setFormatter(consoleformatter)

# when = 
# H-hours
# M-minutes
# S-second
# w0-monday
# w1-tuesday
# d-daily
# midnight

filehandler = TimedRotatingFileHandler("test.log", backupCount=100, when="s", interval=1)
filehandler.setFormatter(consoleformatter)

# filehandler = RotatingFileHandler("test.log", maxBytes=1024, backupCount=100)
# filehandler.setFormatter(consoleformatter)

filehandler.namer = lambda name: name.replace(".log", "")+".log"
logger.addHandler(consolehandler)
logger.addHandler(filehandler)

logger.info("It is a Info log")
logger.warning("It is a Warning log")

try:
    x=1/0
except Exception as e:
    logger.error("Some error occured", exc_info=e)