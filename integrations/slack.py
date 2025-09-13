import os
from slack_sdk import WebClient

class SlackClient:
    def __init__(self):
        self.client = WebClient(token=os.getenv("SLACK_BOT_TOKEN"))

    def send_message(self, channel, text):
        response = self.client.chat_postMessage(channel=channel, text=text)
        return response.data
