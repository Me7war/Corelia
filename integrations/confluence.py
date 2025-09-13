import os
import requests

class ConfluenceClient:
    def __init__(self):
        self.base_url = os.getenv("CONFLUENCE_URL")
        self.auth = (os.getenv("CONFLUENCE_USER"), os.getenv("CONFLUENCE_TOKEN"))

    def get_pages(self, space):
        url = f"{self.base_url}/rest/api/space/{space}/content"
        resp = requests.get(url, auth=self.auth)
        resp.raise_for_status()
        return resp.json().get("results", [])
