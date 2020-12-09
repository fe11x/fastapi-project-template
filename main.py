import logging

from fastapi import FastAPI, Depends

from app import db
from http_helpers import verify_auth_key
from routers import my

logger = logging.getLogger(__name__)


app = FastAPI()


# Configure ORM
db.generate()


# Register routers
app.include_router(
    my.router,
    prefix="/my",
    tags=["user"],
    dependencies=[Depends(verify_auth_key)]
)


@app.get("/error")
def error():
    """
    Used for testing 500 errors
    """
    return 1 / 0
