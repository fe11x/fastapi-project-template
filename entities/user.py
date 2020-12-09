from uuid import UUID

from .base import BaseEntity


class User(BaseEntity):
    id: UUID
    email: str = None
