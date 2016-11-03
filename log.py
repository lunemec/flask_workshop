import sys
import logging
from pythonjsonlogger import jsonlogger


def register_log(app):
    handler = logging.StreamHandler(stream=sys.stdout)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(jsonlogger.JsonFormatter())

    # Promazat stavajici handlery (pokud je nechceme).
    for h in app.logger.handlers:
        app.logger.removeHandler(h)

    app.logger.addHandler(handler)