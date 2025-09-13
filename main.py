from fastapi import FastAPI
from auth import router as auth_router
from agents.finance import router as finance_router
from agents.hr import router as hr_router
from agents.it import router as it_router
from agents.security import router as security_router
from workflows.runner import router as workflow_router


from integrations.openllori import router as openllori_router

app = FastAPI(title="Corelia Enterprise AI Orchestrator")

app.include_router(auth_router, prefix="/auth")
app.include_router(finance_router, prefix="/agents/finance")
app.include_router(hr_router, prefix="/agents/hr")
app.include_router(it_router, prefix="/agents/it")
app.include_router(security_router, prefix="/agents/security")
app.include_router(workflow_router, prefix="/workflows")
app.include_router(openllori_router, prefix="/v1")
