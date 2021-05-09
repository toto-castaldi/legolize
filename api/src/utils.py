from PIL import Image
import logging
import os

LOG_LEVELS = {
    'INFO': 20,
    'DEBUG': 10,
    'WARNING': 30,
    'ERROR': 40,
    'CRITICAL': 50
}

log_level = LOG_LEVELS.get(os.environ.get('LOG_LEVEL', 'INFO'))

logger_handler = False


def init_log():

    global logger_handler

    logger = logging.getLogger()
    logger.setLevel(log_level)

    if logger_handler is False:
        ch = logging.StreamHandler()
        ch.setLevel(log_level)

        formatter = logging.Formatter('[%(levelname)s] %(message)s')
        ch.setFormatter(formatter)

        logger.addHandler(ch)

        logger_handler = True

    return logger

# https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()
