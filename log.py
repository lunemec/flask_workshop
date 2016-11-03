import sys
import logging
from pythonjsonlogger import jsonlogger

from app import app

handler = logging.StreamHandler(stream=sys.stdout)
handler.setLevel(logging.DEBUG)
handler.setFormatter(jsonlogger.JsonFormatter())

# Promazat stavajici handlery (pokud je nechceme).
for h in app.logger.handlers:
    app.logger.removeHandler(h)

app.logger.addHandler(handler)