
<div align="center">
	<h1>📡 API Reference</h1>
	<img src="https://img.icons8.com/color/96/api.png" alt="API"/>
</div>

Corelia exposes a FastAPI backend with the following main endpoints:

- `/auth/token` — JWT login
- `/agents/<agent>/ask` — Query an agent
- `/workflows/run` — Run a workflow
- `/v1/chat/completions` — OpenAI-compatible endpoint (OpenLlori)

See OpenAPI docs at `/docs` when running the server.