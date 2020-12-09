import uuid

from pony.orm import db_session
from pytest_bdd import given, parsers

from app import db
from models.user import User


# Configure ORM
db.generate()


@db_session
def get_or_create_user(**kwargs):
    # This could be done with something like User.select(**kwargs).first() or User(**kwargs)
    # but select with argument does not work, even though docs are saying that it is working since 0.7.7 (we are on 0.7.13+)

    for u in User.select()[:]:
        if all(str(getattr(u, field)) == str(value) for field, value in kwargs.items()):
            return u

    kwargs['id'] = str(uuid.uuid4())
    kwargs['email'] = kwargs.get('email', 'test@example.com')
    return User(**kwargs)


@given(parsers.cfparse("user with email {email}"))
def user_has_some_posts(email):
    user_instance = get_or_create_user(email=email)
    return user_instance
