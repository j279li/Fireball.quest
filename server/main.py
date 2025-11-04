from fastapi import Depends, FastAPI, HTTPException, WebSocket, WebSocketDisconnect, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated
from argon2 import PasswordHasher
from argon2.exceptions import VerificationError
from datetime import datetime, timedelta, UTC
import jwt
from jwt.exceptions import InvalidTokenError
from collections import defaultdict

# TODO: move into env
JWT_KEY = "4333ba51130b668637a762adf7e200f37a2760b6e49dc9cdcfce853146d2a1e3"
JWT_ALGORITHM = "HS256"

password_hasher = PasswordHasher()

# in-memory user store for now
users = {
    "JohnDoe": {
        "username": "JohnDoe",
        "password": password_hasher.hash("password1")
    },
    "ArenaCloser": {
        "username": "ArenaCloser",
        "password": password_hasher.hash("diep!")
    }
}

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    try:
        claims = jwt.decode(token, JWT_KEY, algorithms=[JWT_ALGORITHM])
        username = claims.get("sub")
        if username not in users:
            raise InvalidTokenError
        return users[username]
    except InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"}
        )

@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    bad_credentials = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Bad credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    if form_data.username not in users:
        raise bad_credentials
    user = users[form_data.username]
    try:
        password_hasher.verify(user["password"], form_data.password)
    except VerificationError:
        raise bad_credentials
    return {
        "access_token": jwt.encode({
            "sub": form_data.username, "exp": datetime.now(UTC) + timedelta(hours=1)
        }, JWT_KEY, JWT_ALGORITHM),
        "token_type": "bearer"
    }


active_connections = defaultdict(set)

@app.websocket("/chat/{chat_id}")
async def chat(websocket: WebSocket, chat_id: str):
    user = await get_current_user(websocket.query_params.get("token"))
    await websocket.accept()
    active_connections[chat_id].add(websocket)
    try:
        while True:
            text = await websocket.receive_text()
            for connection in active_connections[chat_id]:
                await connection.send_json({
                    "message": text,
                    "username": user["username"]
                })
    except WebSocketDisconnect:
        active_connections[chat_id].remove(websocket)
