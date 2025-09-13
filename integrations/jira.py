import os
from jira import JIRA

class JiraClient:
    def __init__(self):
        self.jira = JIRA(
            server=os.getenv("JIRA_SERVER"),
            basic_auth=(os.getenv("JIRA_USER"), os.getenv("JIRA_TOKEN"))
        )

    def get_issues(self, jql):
        issues = self.jira.search_issues(jql)
        return [issue.key for issue in issues]
