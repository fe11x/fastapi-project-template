from uuid import UUID

from pony.orm import PrimaryKey, Optional
from app.db import db


class User(db.Entity):
    id = PrimaryKey(UUID, auto=True)
    email = Optional(str)
