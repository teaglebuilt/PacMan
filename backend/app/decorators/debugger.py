from logging.handlers import TimedRotatingFileHandler
import functools
import logging
import sys
FORMATTER = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")
LOG_FILE = "logs/debug.log"



def debug(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return_value = func(*args, **kwargs)
        logger.debug(f'Calling : {func.__name__}')
        logger.debug(f'args, kwargs: {args, kwargs}')
        logger.debug(f'{func.__name__} returned {return_value}')

        return return_value

    return wrapper



class Debugger(object):

    enabled = False

    def __init__(self, func):
        self.func = func
        self.logger = self.get_logger("debugger")

    def get_console_handler(self):
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(FORMATTER)
        return console_handler

    def get_file_handler(self):
        file_handler = TimedRotatingFileHandler(LOG_FILE, when='midnight')
        file_handler.setFormatter(FORMATTER)
        return file_handler

    def get_logger(self, logger_name):
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG) 
        logger.addHandler(self.get_console_handler())
        logger.addHandler(self.get_file_handler())
        logger.propagate = False
        return logger

    def __call__(self, *args, **kwargs):
        if self.enabled:
            self.logger.debug(f'Entering : {self.func.__name__}')
            self.logger.debug(f'args, kwargs : {args, kwargs}')
            self.logger.debug(f'{self.func.__name__} returned : {self.func(*args, **kwargs)}')
        return self.func(*args, **kwargs)