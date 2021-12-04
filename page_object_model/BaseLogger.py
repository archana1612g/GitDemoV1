import inspect
import logging


class logclass:
    def get_logger(self):
        log = inspect.stack()[1][3]
        logger = logging.getLogger(log)
        handle = logging.FileHandler("logfile.log")
        form = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s ")
        handle.setFormatter(form)
        logger.addHandler(handle)

        logger.setLevel(logging.DEBUG)
        return logger
