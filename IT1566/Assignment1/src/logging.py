import sys
import logging
import datetime

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a handler that will save logs to a file
logger_handler = logging.FileHandler(
    filename="core.log", encoding="utf-8")
logger_handler.setLevel(logging.DEBUG)

# Create a formatter for saved logs and add it to the handler
logging_formatter = logging.Formatter("%(message)s")
logger_handler.setFormatter(logging_formatter)

# Now add the handler to the original logger
logger.addHandler(logger_handler)
logging.info("Logger configured successfully!")

class LoggingHandler():
    """
    Custom exceptions handler to handle errors found during runtime in the interpreter

    Args:
        source (str): The current script that has initialized the function (recommended to use __name__ when initializing)
        
    Log format:
        [timestamp] - [origin]:[log_level] - [log_message]
    """
    def __init__(self, source: str):
        self.logger: logging.Logger = logging.getLogger(__name__)
        self.source: str = source
        
        
        
    def get_log_time(self):
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def raise_exception(self, error_msg: str) -> bool:
        """
        Throws a custom exception. For logging levels of error or higher

        Args:
            error_msg (str): The error message to be displayed
        
        Returns:
            bool: True if the log entry was successfully created, False otherwise
        """
        try:
            self.logger.error(f"{self.get_log_time()} - {self.source}:ERROR - {error_msg}")
            return True
        except Exception as e:
            return False
        
    def create_log(self, log_msg: str, log_lvl: int = 0) -> bool:
        """
        Generates a log entry with the source location
        
        Args:
            log_lvl (str): The log level to be used. Default is 0 (for DEBUG)
                - 0: DEBUG
                - 1: INFO
                - 2: WARNING
            log_msg (str): The log message to be displayed
        
        Returns:
            bool: True if the log entry was successfully created, False otherwise
        """
        try:
            if log_lvl == 0: 
                self.logger.debug(f"{self.get_log_time()} - {self.source}:DEBUG - {log_msg}")
            elif log_lvl == 1:
                self.logger.info(f"{self.get_log_time()} - {self.source}:INFO - {log_msg}")
            elif log_lvl == 2:
                self.logger.warning(f"{self.get_log_time()} - {self.source}:WARNING - {log_msg}")
            else:
                return False
            return True
        except Exception as e:
            return False