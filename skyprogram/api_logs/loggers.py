import logging


def create_api_logger():
    api_logger = logging.getLogger("api_logger")
    api_logger.setLevel("DEBUG")

    api_logger_handler = logging.FileHandler("logs/api.log")
    api_logger_handler.setLevel("DEBUG")

    api_logger.addHandler(api_logger_handler)

    #Форматтеры
    LOGGER_FORMAT = f"%(asctime)s - [%(levelname)s] - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
    api_logger_format = logging.Formatter(LOGGER_FORMAT)

    api_logger_handler.setFormatter(api_logger_format)
