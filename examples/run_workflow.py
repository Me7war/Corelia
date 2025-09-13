import requests
import getpass

BASE_URL = "http://localhost:8000"

username = input("Username: ")
password = getpass.getpass("Password: ")

resp = requests.post(f"{BASE_URL}/auth/token", data={"username": username, "password": password})
token = resp.json()["access_token"]
headers = {"Authorization": f"Bearer {token}"}

workflow = input("Workflow name (daily_report/jira_to_slack): ")
r = requests.post(f"{BASE_URL}/workflows/run", json={"workflow_name": workflow}, headers=headers)
print(r.json())
