from fastapi import APIRouter, Depends
from agents.base import BaseAgent
from auth import get_current_user

router = APIRouter()


import os
agent = BaseAgent(name="SecurityAgent", model=os.getenv("SECURITY_MODEL", "llama3"))

@router.post("/ask")
def ask_security(prompt: str, user=Depends(get_current_user)):
    return {"response": agent.ask(prompt)}
