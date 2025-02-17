import logging

class Logger:
    def __init__(self):
        logging.basicConfig(filename="operations.log", level=logging.INFO)

    def log(self, message: str):
        logging.info(message)
