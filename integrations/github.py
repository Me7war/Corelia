import os
from github import Github

class GitHubClient:
    def __init__(self):
        self.gh = Github(os.getenv("GITHUB_TOKEN"))

    def get_repos(self, user):
        user_obj = self.gh.get_user(user)
        return [repo.name for repo in user_obj.get_repos()]
