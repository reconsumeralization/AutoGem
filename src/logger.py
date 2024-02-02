import logging

DEFAULT_LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DEFAULT_LOG_LEVEL = logging.INFO
DEFAULT_LOG_FILE = "application.log"

def setup_logger(name, log_file=DEFAULT_LOG_FILE, log_level=DEFAULT_LOG_LEVEL, enable_console=True):
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    formatter = logging.Formatter(DEFAULT_LOG_FORMAT)

    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(log_level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    if enable_console:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger
