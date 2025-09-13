import threading

class InMemoryCache:
    def __init__(self):
        self.lock = threading.Lock()
        self.store = {}

    def set(self, key, value):
        with self.lock:
            self.store[key] = value

    def get(self, key):
        with self.lock:
            return self.store.get(key)

cache = InMemoryCache()
