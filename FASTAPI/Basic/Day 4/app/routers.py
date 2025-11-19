from fastapi import APIRouter, Header, HTTPException, status
from .schemas import LoginRequest, ProfileResponse
from .services import authenticate_user, validate_token

router = APIRouter()

@router.post("/login", response_model=dict)
def login(credentials: LoginRequest):
    token = authenticate_user(credentials.username, credentials.password)
    if token is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return {"access_token": token, "token_type": "bearer"}

@router.get("/profile", response_model=ProfileResponse)
def profile(authorization: str | None = Header(None)):
    username = validate_token(authorization)
    if username is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or missing token")
    return ProfileResponse(username=username, email=f"{username}@example.com")
