from fastapi import APIRouter, Depends
from agents.base import BaseAgent
from auth import get_current_user

router = APIRouter()


import os
agent = BaseAgent(name="FinanceAgent", model=os.getenv("FINANCE_MODEL", "llama3"))

@router.post("/ask")
def ask_finance(prompt: str, user=Depends(get_current_user)):
    return {"response": agent.ask(prompt)}
