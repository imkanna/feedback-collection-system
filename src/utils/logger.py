import logging
from os import makedirs
from os.path import abspath, join, dirname, exists
from logging.handlers import RotatingFileHandler

from src.server.application_context import LoggerConfiguration

class Logger:
    LOG_FILE_NAME = 'feedback_collector_api.log'
    FORMATTING_STRING = '%(asctime)s %(process)d [%(levelname)s] %(message)s'
    LOG_LEVEL = logging.INFO
    MAX_BYTES = (1024 ** 2) * 100  # 100MB
    BACKUP_COUNT = 5  # Keep up to server.log.5

    @classmethod
    def initiate_logger(cls, logger_configs: LoggerConfiguration):
        handlers = []

        # file logging handler
        log_file = f'{abspath(join(dirname(__file__), "../.."))}/logs/{cls.LOG_FILE_NAME}'
        # Create file and directory if they don't exist
        cls.__create_file(log_file)
        handlers.append(RotatingFileHandler(log_file, maxBytes=cls.MAX_BYTES, backupCount=cls.BACKUP_COUNT))
        # Console logging handler
        handlers.append(logging.StreamHandler())
        # Configure
        logging.basicConfig(format=cls.FORMATTING_STRING, level=cls.__get_log_level(logger_configs.log_level), handlers=handlers)


    def __init__(self, class_name):
        self._logger = logging.getLogger(class_name)

    def info(self, message):
        self._logger.info(message)

    def error(self, message, exc_info=True):
        self._logger.exception(message, exc_info=exc_info)

    def debug(self, message):
        self._logger.debug(message)

    def warn(self, message):
        self._logger.warn(message)

    @classmethod
    def __create_file(cls, log_file: str):
        dir_name = log_file.replace(f'/{cls.LOG_FILE_NAME}', '')
        if not exists(dir_name): makedirs(dir_name)
        if not exists(log_file): open(log_file, 'w').close()

    @classmethod
    def __get_log_level(cls, level_name: str):
        if not level_name:
            return cls.LOG_LEVEL

        level_name_upper = level_name.upper()
        return logging.getLevelName(level_name_upper)