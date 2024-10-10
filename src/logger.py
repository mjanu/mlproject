import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True) # creating new file everytime logging happned

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,  # File to write logs to (default is None for console output)
    format="%(asctime)s  %(lineno)d %(name)s - %(levelname)s -%(message)s",
    level=logging.INFO, #Sets the logging level, controlling which severity of logs are handled. INFO-General information



)

