from typing import Optional
_users = {
    "alice": "wonderland",
    "sam": "password123",
}

FAKE_TOKEN_PREFIX = "Bearer fake-token-"


def authenticate_user(username: str, password: str) -> Optional[str]:
    if _users.get(username) == password:
        return FAKE_TOKEN_PREFIX + username
    return None


def validate_token(authorization: str | None) -> Optional[str]:
    if authorization is None or not authorization.startswith(FAKE_TOKEN_PREFIX):
        return None
    return authorization[len(FAKE_TOKEN_PREFIX):]
