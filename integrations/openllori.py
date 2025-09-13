import os
from fastapi import APIRouter, Request, HTTPException, Depends
from fastapi.responses import JSONResponse
from auth import get_current_user
import requests

router = APIRouter()

OLLAMA_SERVER_URL = os.getenv("OLLAMA_SERVER_URL", "http://localhost:11434")
API_KEYS = os.getenv("API_KEYS", "").split(",")
RATE_LIMIT = int(os.getenv("RATE_LIMIT", 60))

# Simple in-memory rate limit (per key)
from memory.cache import cache
import time

def check_rate_limit(api_key):
    now = int(time.time())
    key = f"ratelimit:{api_key}:{now//60}"
    count = cache.get(key) or 0
    if count >= RATE_LIMIT:
        raise HTTPException(status_code=429, detail="Rate limit exceeded")
    cache.set(key, count + 1)

@router.post("/v1/chat/completions")
def chat_completions(request: Request):
    api_key = request.headers.get("Authorization", "").replace("Bearer ", "")
    if api_key not in API_KEYS:
        raise HTTPException(status_code=401, detail="Invalid API key")
    check_rate_limit(api_key)
    data = request.json()
    model = data.get("model", "llama3")
    messages = data.get("messages", [])
    # Forward to Ollama
    ollama_url = f"{OLLAMA_SERVER_URL}/v1/chat/completions"
    resp = requests.post(ollama_url, json={"model": model, "messages": messages})
    return JSONResponse(content=resp.json(), status_code=resp.status_code)
