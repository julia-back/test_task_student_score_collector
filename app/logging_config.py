"""
Прослушивание логов запускается и останавливается с FastAPI-приложением
в lifespan
"""

import logging
from queue import Queue
from logging.handlers import QueueHandler, QueueListener
from logging import FileHandler, StreamHandler


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

queue_for_logger = Queue()

queue_handler = QueueHandler(queue_for_logger)
logger.addHandler(queue_handler)

file_handler = FileHandler("logs.txt")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
file_handler.setLevel(logging.WARNING)

stream_handler = StreamHandler()
stream_formatter = logging.Formatter("%(levelname)s - %(name)s - %(message)s")
stream_handler.setFormatter(stream_formatter)
stream_handler.setLevel(logging.DEBUG)

logging_queue_listener = QueueListener(queue_for_logger,
                                       file_handler, stream_handler,
                                       respect_handler_level=True)
