import logging


def setup_logger(name: str = "app") -> logging.Logger:
    """Sets up and returns a logger with the specified name.

    If a logger with the same name already exists, it is reused.
    Otherwise, a new logger is created and configured to log to stdout
    with the format:
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    The default log level is INFO.

    Args:
        name (str): The name of the logger. Defaults to "app".

    Returns:
        logging.Logger: The configured logger instance.
    """
    logger: logging.Logger = logging.getLogger(name)

    if not logger.hasHandlers():
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

    return logger
