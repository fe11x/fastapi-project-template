import os
import logging
import sys


AUTO_CREATE_DB = os.environ.get('AUTO_CREATE_DB', True)

DATABASE = {
    'provider': 'postgres',
    'user': os.environ.get('DB_USER', 'postgres'),
    'password': os.environ.get('DB_PASS', ''),
    'host': os.environ.get('DB_HOST', 'localhost'),
    'database': os.environ.get('DB_NAME', 'test')
}


logging.basicConfig(stream=sys.stdout, level=logging.INFO)

try:
    from .local import *
except ImportError:
    pass
