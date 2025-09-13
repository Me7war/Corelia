
<div align="center">
	<h1>🤖 Agents</h1>
	<img src="https://img.icons8.com/color/96/robot-2.png" alt="Agents"/>
</div>

Corelia agents are specialized AI services, each wrapping a local transformer model via Ollama. Agents include:
- **FinanceAgent**
- **HRAgent**
- **ITAgent**
- **SecurityAgent**

## Agent API
Each agent exposes an `/ask` endpoint for chat and a `use_tool` method for integrations.

## Implementation
- Agents use the Ollama API for LLM inference.
- Each agent can remember context (vector DB, cache).
- Tools: Slack, Jira, GitHub, Confluence.

See each agent's Python file for details.