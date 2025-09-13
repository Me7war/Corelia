import requests
import getpass

BASE_URL = "http://localhost:8000"

username = input("Username: ")
password = getpass.getpass("Password: ")

resp = requests.post(f"{BASE_URL}/auth/token", data={"username": username, "password": password})
token = resp.json()["access_token"]
headers = {"Authorization": f"Bearer {token}"}

agent = input("Agent (finance/hr/it/security): ")
prompt = input("Prompt: ")

r = requests.post(f"{BASE_URL}/agents/{agent}/ask", json={"prompt": prompt}, headers=headers)
print(r.json())
