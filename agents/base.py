from typing import Any, Dict

import os
import requests
from memory.vectordb import upsert_vector, search_vector
from memory.cache import cache
from config import settings

class BaseAgent:
    def __init__(self, name: str, model: str):
        self.name = name
        self.model = model
        self.ollama_url = os.getenv("OLLAMA_SERVER_URL", settings.OLLAMA_URL)

    def ask(self, prompt: str) -> str:
        # Real Ollama call
        resp = requests.post(f"{self.ollama_url}/v1/chat/completions", json={
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}]
        })
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"]

    def remember(self, key: str, value: Any):
        # Store in vector DB and cache
        upsert_vector(key, value if isinstance(value, list) else [float(value)], payload={"agent": self.name})
        cache.set(key, value)

    def use_tool(self, tool_name: str, params: Dict[str, Any]) -> Any:
        # Tool dispatch (example: Slack, Jira, etc.)
        if tool_name == "slack":
            from integrations.slack import SlackClient
            return SlackClient().send_message(**params)
        elif tool_name == "jira":
            from integrations.jira import JiraClient
            return JiraClient().get_issues(**params)
        elif tool_name == "github":
            from integrations.github import GitHubClient
            return GitHubClient().get_repos(**params)
        elif tool_name == "confluence":
            from integrations.confluence import ConfluenceClient
            return ConfluenceClient().get_pages(**params)
        else:
            raise ValueError(f"Unknown tool: {tool_name}")
