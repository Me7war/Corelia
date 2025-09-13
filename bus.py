import os
import redis
import json

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
r = redis.Redis.from_url(REDIS_URL)

def publish(channel: str, message: dict):
    r.publish(channel, json.dumps(message))

def subscribe(channel: str):
    pubsub = r.pubsub()
    pubsub.subscribe(channel)
    return pubsub
