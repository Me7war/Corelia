
<div align="center">
	<h1>Corelia — Enterprise AI Orchestrator</h1>
	<a href="https://github.com/UnexpectedNull/Corelia"><img src="https://img.shields.io/github/stars/UnexpectedNull/Corelia?style=social" alt="GitHub stars"></a>
	<a href="https://github.com/UnexpectedNull/Corelia"><img src="https://img.shields.io/github/forks/UnexpectedNull/Corelia?style=social" alt="GitHub forks"></a>
	<a href="https://github.com/UnexpectedNull/Corelia"><img src="https://img.shields.io/github/issues/UnexpectedNull/Corelia" alt="GitHub issues"></a>
	<br>
	<a href="https://github.com/UnexpectedNull/Corelia">🌐 GitHub Repo</a>
</div>



<p align="center">
	<img src="https://img.icons8.com/color/96/artificial-intelligence.png" alt="AI"/>
	<img src="https://img.icons8.com/color/96/robot-2.png" alt="Agents"/>
	<img src="https://img.icons8.com/color/96/database.png" alt="Database"/>
	<img src="https://img.icons8.com/color/96/workflow.png" alt="Workflow"/>
</p>

## Overview
<b>Corelia</b> is an enterprise backend orchestrator for AI agents (Finance, HR, IT, Security), each wrapping a local transformer model (Ollama/llama.cpp). Agents collaborate via a message bus, store context in a vector DB, and execute configurable workflows. Includes secure authentication, agent APIs, workflow runner, enterprise integrations, and usage examples.

## 📚 [Documentation](docs/README.md)

<p align="center">
	<a href="docs/README.md"><img src="https://img.icons8.com/color/48/open-book--v2.png" alt="Docs"/></a>
</p>

## 🗺️ Architecture Diagram
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
- **Agent Communication**: Redis pub/sub
- **Memory**: Qdrant/Weaviate + in-memory cache
- **Workflows**: YAML/JSON runner
- **Integrations**: Slack, Jira, GitHub, Confluence
- **Persistence**: PostgreSQL/SQLite logs

---

## 🚀 Quickstart

### 1. Clone & Install
```bash
git clone https://github.com/UnexpectedNull/Corelia.git
cd Corelia
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```


### 2. Configure
Edit `.env` for Ollama, DB, Redis, Qdrant, and OpenLlori keys:

```
OLLAMA_SERVER_URL=http://localhost:11434
API_KEYS=yourkey1,yourkey2
PORT=8000
RATE_LIMIT=60
```

### 3. Start Services
```bash
docker-compose up -d
```

### 4. Run API
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### 5. Try Examples
```bash
cd examples
python query_agent.py
python run_workflow.py
```

---

## ⚡ OpenLlori Quickstart

Install dependencies:
```bash
pip install -r requirements.txt
```

Configure `.env`:
```
OLLAMA_SERVER_URL=http://localhost:11434
API_KEYS=yourkey1,yourkey2
PORT=8000
RATE_LIMIT=60
```

Start the server:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

Call the API (Python example):
```python
import openai
openai.api_key = "yourkey1"
openai.api_base = "http://localhost:8000/v1"
response = openai.ChatCompletion.create(
	model="llama3",
	messages=[{"role": "user", "content": "Hello!"}]
)
print(response)
```

---

## 🗂️ Project Structure
```
main.py                # FastAPI entrypoint, routes
auth.py                # JWT + role-based access
agents/                # Agent logic (base + specializations)
workflows/             # Workflow runner + YAMLs
integrations/          # Slack, Jira, GitHub, Confluence
memory/                # Vector DB + cache
bus.py                 # Redis pub/sub
config.py              # Env loader
db.py                  # Logging (Postgres/SQLite)
requirements.txt       # Backend deps
docker-compose.yml     # Redis, Postgres, Qdrant
examples/              # Usage scripts
```

---

## 📝 Notes
- Agents use real Ollama and API integrations. Configure `.env` for all service tokens and endpoints.
- For production, use PostgreSQL and secure secrets.
- Extend workflows and integrations as needed.
