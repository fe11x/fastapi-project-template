from pony.orm import Database
from . import settings


db = Database()
db.bind(**settings.DATABASE)


def generate():
    # Need to import all of the models to init it and add to mapping
    from models import user
    db.generate_mapping(create_tables=settings.AUTO_CREATE_DB)
