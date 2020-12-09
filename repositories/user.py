from uuid import UUID

from pony.orm import db_session

import entities

from models.user import User
from .orm_tools import mapper


@db_session
@mapper(entity=entities.User, config={"code": "email_code"})
def get_user(user_id: UUID):
    return User.get(id=user_id)


@db_session
def does_email_exist(email: str) -> bool:
    return User.exists(email=email)


@db_session
def delete_user_by_email(email: str):
    return User.get(email=email).delete()
