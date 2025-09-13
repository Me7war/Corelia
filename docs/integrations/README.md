
<div align="center">
	<h1>🔗 Integrations</h1>
	<img src="https://img.icons8.com/color/96/api-settings.png" alt="Integrations"/>
</div>

Corelia integrates with enterprise tools:
- **Slack**: Send messages to channels.
- **Jira**: Query issues, tickets.
- **GitHub**: List repositories, interact with code.
- **Confluence**: Fetch pages, documentation.

## Configuration
Set API tokens and endpoints in `.env`:
- `SLACK_BOT_TOKEN`
- `JIRA_SERVER`, `JIRA_USER`, `JIRA_TOKEN`
- `GITHUB_TOKEN`
- `CONFLUENCE_URL`, `CONFLUENCE_USER`, `CONFLUENCE_TOKEN`

See each integration's Python file for usage.