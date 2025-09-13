
<div align="center">
	<h1>Corelia Architecture Overview</h1>
	<img src="https://img.icons8.com/color/96/artificial-intelligence.png" alt="AI"/>
	<img src="https://img.icons8.com/color/96/robot-2.png" alt="Agents"/>
	<img src="https://img.icons8.com/color/96/database.png" alt="Database"/>
	<img src="https://img.icons8.com/color/96/workflow.png" alt="Workflow"/>
</div>

Corelia is an enterprise AI orchestrator backend that manages multiple specialized AI agents, each wrapping a local transformer model (Ollama/llama.cpp). Agents collaborate via a message bus, store context in a vector database, and execute configurable workflows. The backend provides secure authentication, agent APIs, workflow execution, integrations, and logging.

## Architecture Diagram
```mermaid
flowchart TD
	subgraph API
		A1[FastAPI Backend]
		A2[JWT Auth & RBAC]
	end
	subgraph Agents
		B1[FinanceAgent]
		B2[HRAgent]
		B3[ITAgent]
		B4[SecurityAgent]
	end
	subgraph Integrations
		C1[Slack]
		C2[Jira]
		C3[GitHub]
		C4[Confluence]
	end
	subgraph Memory
		D1[Qdrant/Weaviate]
		D2[In-Memory Cache]
	end
	subgraph Infra
		E1[Redis Pub/Sub]
		E2[Postgres/SQLite]
		E3[Ollama Server]
	end
	A1 --> B1
	A1 --> B2
	A1 --> B3
	A1 --> B4
	B1 -- Ollama --> E3
	B2 -- Ollama --> E3
	B3 -- Ollama --> E3
	B4 -- Ollama --> E3
	B1 -- Memory --> D1
	B2 -- Memory --> D1
	B3 -- Memory --> D1
	B4 -- Memory --> D1
	B1 -- Cache --> D2
	B2 -- Cache --> D2
	B3 -- Cache --> D2
	B4 -- Cache --> D2
	B1 -- Pub/Sub --> E1
	B2 -- Pub/Sub --> E1
	B3 -- Pub/Sub --> E1
	B4 -- Pub/Sub --> E1
	B1 -- Tools --> C1
	B1 -- Tools --> C2
	B1 -- Tools --> C3
	B1 -- Tools --> C4
	B2 -- Tools --> C1
	B2 -- Tools --> C2
	B2 -- Tools --> C3
	B2 -- Tools --> C4
	B3 -- Tools --> C1
	B3 -- Tools --> C2
	B3 -- Tools --> C3
	B3 -- Tools --> C4
	B4 -- Tools --> C1
	B4 -- Tools --> C2
	B4 -- Tools --> C3
	B4 -- Tools --> C4
	A1 --> B1
	A1 --> B2
	A1 --> B3
	A1 --> B4
	A1 -- Logs --> E2
```
- **Integrations**: Slack, Jira, GitHub, Confluence connectors.
- **Persistence**: PostgreSQL/SQLite for logs and activity.
- **API**: FastAPI-based, JWT authentication, RBAC.

See subfolders for details on each component.