
<div align="center">
  <h1>🔄 Workflows</h1>
  <img src="https://img.icons8.com/color/96/workflow.png" alt="Workflow"/>
</div>

Workflows in Corelia are defined in YAML/JSON and executed by the workflow runner. Each workflow consists of steps, each step calling an agent or tool.

## Example
```yaml
name: Jira to Slack
steps:
  - agent: ITAgent
    action: use_tool
    tool: jira
    input: "Get all open Jira issues assigned to IT."
  - agent: ITAgent
    action: use_tool
    tool: slack
    input: "Send summary to #it-team."
```

## Running Workflows
Use the `/workflows/run` API or `examples/run_workflow.py` script.