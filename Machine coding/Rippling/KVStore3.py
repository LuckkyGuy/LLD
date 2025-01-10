class KVStore:
    def __init__(self):
        self.store = {}
        self.transaction_active = False
        self.stack = []
    
    def begin(self):
        self.stack.append(self.store.copy())
        self.transaction_active = True

    def set_value(self, key, value):
        if self.transaction_active:
            self.stack[-1][key] = value    
        else:
            self.store[key] = value
    
    def __get_value_helper(self, key, store):
        if key not in store:
            print("Key not found")
            return None
        return store[key]
    
    def get_value(self, key):
        if self.stack:
            return self.__get_value_helper(key, self.stack[-1])
        else:
            return self.__get_value_helper(key, self.store)

    def rollback(self):
        if not self.stack:
            return
        self.stack.pop()

    def commit(self):
        if not self.stack:
            print("Nothing to commit")
            return None
        temp_store = self.stack.pop()
        for key, value in temp_store.items():
            if value != None:
                self.store[key] = value
            else:
                self.store.pop(key, None)                

    def delete_key(self, key):
        if not self.stack:
            self.store.pop(key, None)
        else:
            self.stack[-1][key] = None


kv = KVStore()
kv.set_value(1,2)
kv.begin()
kv.set_value(2,4)
kv.begin()
kv.set_value(3,6)
print(kv.get_value(1))
print(kv.get_value(3))
kv.commit()
print(kv.get_value(2))