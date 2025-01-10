
import threading
class KVStore:
    def __init__(self):
        self.store = {}
        self.lock= threading.lock()
    
    def set_value(self, key, value):
        with self.lock():
            self.store[key] = value
    
    def get_value(self, key):
        if key not in self.store:
            raise Exception("Invalid Key")
        return self.store[key]
    
    def delete_key(self, key):
        if key not in self.store:
            raise Exception("Invalid Key")
        
        del self.store[key]

thread = threading.Thread(target=increment)