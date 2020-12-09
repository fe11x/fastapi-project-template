from pydantic import BaseModel


class BaseEntity(BaseModel):
    """
    Base entity for ORM models
    """
    class Config:
        orm_mode = True
