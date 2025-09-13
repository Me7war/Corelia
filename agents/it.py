from fastapi import APIRouter, Depends
from agents.base import BaseAgent
from auth import get_current_user

router = APIRouter()


import os
agent = BaseAgent(name="ITAgent", model=os.getenv("IT_MODEL", "llama3"))

@router.post("/ask")
def ask_it(prompt: str, user=Depends(get_current_user)):
    return {"response": agent.ask(prompt)}
