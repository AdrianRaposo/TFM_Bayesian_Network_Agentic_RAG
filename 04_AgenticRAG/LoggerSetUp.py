# LoggerSetUp.py
'''
LoggerSetUp.py
This module sets up a logger for the Data Ingestion process.
It configures two handlers: one for general logs and another specifically for errors.   

This allows for better separation of log messages, making it easier to debug and monitor the process.
'''
import logging
import os

# Setup logger function
def setup_logger(
    name: str,
    logs_base_path: str ,
    general_log_filename: str,
    error_log_filename: str,
    general_level,
    error_level,
    general_mode,
    error_mode
):
    """
    Configures a logger with two handlers: one general and another only for errors.

    :param name: Logger name (usually use '__name__').
    :param logs_base_path: Folder where logs are saved.
    :param general_log_filename: File for general logs.
    :param error_log_filename: File for error logs.
    :param general_level: General logs level.
    :param error_level: Error logs level.
    :param general_mode: Opening mode for general file ('w' to overwrite, 'a' to append).
    :param error_mode: Opening mode for error file ('w' to overwrite, 'a' to append).
    :return: configured logger.
    """
    os.makedirs(logs_base_path, exist_ok=True)
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)  # Captures everything, handlers filter
    
    # Avoids adding duplicate handlers
    if not logger.handlers:
        # General handler
        general_handler = logging.FileHandler(
            os.path.join(logs_base_path, general_log_filename), mode=general_mode
        )
        general_handler.setLevel(general_level)
        general_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        logger.addHandler(general_handler)

        # Error-only handler
        error_handler = logging.FileHandler(
            os.path.join(logs_base_path, error_log_filename), mode=error_mode
        )
        error_handler.setLevel(error_level)
        error_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        logger.addHandler(error_handler)

        # Console handler for real-time logging
        console_handler = logging.StreamHandler()
        console_handler.setLevel(general_level)
        console_handler.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))
        logger.addHandler(console_handler)

    return logger
