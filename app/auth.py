from fastapi import Header, HTTPException
from .model import settings

def get_authorization(auth_token: str = Header(None)):
    if auth_token != settings.app_auth_token:
        raise HTTPException(status_code=401, detail="Invalid Authorization Token!")
    return auth_token
