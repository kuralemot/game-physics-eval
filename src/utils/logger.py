import logging
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')
logging.basicConfig(filename=os.getenv("LOG"),
                level=logging.INFO,
                format='%(asctime)s - %(levelname)s - %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S')

def debug(message, silent=False):
    if not silent:
        print(message)
    logging.debug(message)

def info(message, silent=False):
    if not silent:
        print(message)
    logging.info(message)

def warning(message, silent=False):
    if not silent:
        print(message)
    logging.warning(message)

def error(message, silent=False):
    if not silent:
        print(message)
    logging.error(message)

def critical(message, silent=False):
    if not silent:
        print(message)
    logging.critical(message)