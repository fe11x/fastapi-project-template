import os
import logging
import sys


AUTO_CREATE_DB = os.environ.get('AUTO_CREATE_DB', True)

DATABASE = {
    'provider': 'sqlite',
    'filename': os.environ.get('DB_FILE', 'database.sqlite'),
    'create_db': True
}


logging.basicConfig(stream=sys.stdout, level=logging.INFO)

try:
    from .local import *
except ImportError:
    pass
