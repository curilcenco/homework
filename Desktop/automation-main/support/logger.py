import logging
import os


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')


log_file = os.path.join(os.path.dirname(__file__), 'automation.log')
file_handler = logging.FileHandler(log_file)
file_handler.setFormatter(formatter)


if not logger.hasHandlers():
    logger.addHandler(file_handler)