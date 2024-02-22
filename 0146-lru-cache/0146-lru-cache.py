class LRUCache:

    def __init__(self, capacity: int):
        self.orderdict = collections.OrderedDict();
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key not in self.orderdict:
            return -1
        self.orderdict.move_to_end(key, True)
        return self.orderdict[key]

    def put(self, key: int, value: int) -> None:
        if key in self.orderdict:
            self.orderdict.move_to_end(key, True)
        self.orderdict[key] = value
        if len(self.orderdict) > self.capacity:
            self.orderdict.popitem(last=False)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)