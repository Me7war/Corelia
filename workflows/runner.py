import yaml
from fastapi import APIRouter, HTTPException, Depends
from auth import get_current_user
import os

router = APIRouter()


from agents.finance import agent as finance_agent
from agents.hr import agent as hr_agent
from agents.it import agent as it_agent
from agents.security import agent as security_agent

AGENT_MAP = {
    "FinanceAgent": finance_agent,
    "HRAgent": hr_agent,
    "ITAgent": it_agent,
    "SecurityAgent": security_agent,
}

@router.post("/run")
def run_workflow(workflow_name: str, user=Depends(get_current_user)):
    path = os.path.join(os.path.dirname(__file__), "examples", f"{workflow_name}.yaml")
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="Workflow not found")
    with open(path) as f:
        workflow = yaml.safe_load(f)
    steps = workflow.get("steps", [])
    results = []
    for step in steps:
        agent_name = step.get("agent")
        action = step.get("action")
        input_ = step.get("input")
        tool = step.get("tool")
        agent = AGENT_MAP.get(agent_name)
        if not agent:
            results.append({"error": f"Unknown agent: {agent_name}"})
            continue
        if action == "ask":
            result = agent.ask(input_)
        elif action == "use_tool" and tool:
            result = agent.use_tool(tool, {"input": input_})
        else:
            result = {"error": f"Unknown action: {action}"}
        results.append({"agent": agent_name, "action": action, "result": result})
    return {"workflow": workflow_name, "results": results}
