class KVStore:
    def __init__(self):
        self.store = {}
        self.transaction_active = False
    
    def begin(self):
        self.temp_store = self.store.copy()
        self.transaction_active = True

    def set_value(self, key, value):
        if self.transaction_active:
            self.temp_store[key] = value    
        else:
            self.store[key] = value
    
    def __get_value_helper(self, key, store):
        if key not in store:
            print("Key not found")
            return None
        return store[key]
    
    def get_value(self, key):
        if self.transaction_active:
            return self.__get_value_helper(key, self.temp_store)
        else:
            return self.__get_value_helper(key, self.store)

    def rollback(self):
        self.temp_store = None
        self.transaction_active = False

    def commit(self):
        if not self.transaction_active:
            print("Nothing to commit")
            return None
        for key, value in self.temp_store.items():
            if value != None:
                self.store[key] = value
            else:
                self.store.pop(key, None)                
        self.temp_store = None
        self.transaction_active = False
        return True

    def delete_key(self, key):
        if not self.transaction_active:
            self.store.pop(key, None)
        else:
            self.temp_store[key] = None


kv = KVStore()
kv.set_value(1,2)
kv.begin()
kv.set_value(2,4)
print(kv.get_value(1))
print(kv.get_value(2))
kv.commit()
print(kv.get_value(2))