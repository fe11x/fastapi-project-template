import os
from typing import Optional

from fastapi import Header, HTTPException


HTTP_AUTH_KEY = 'HTTP_AUTH_KEY'


def verify_auth_key(auth_key: Optional[str] = Header(None, alias=HTTP_AUTH_KEY, convert_underscores=False)):
    env_key = os.environ.get(HTTP_AUTH_KEY)
    if env_key and auth_key != env_key:
        raise HTTPException(status_code=401, detail="Access denied")