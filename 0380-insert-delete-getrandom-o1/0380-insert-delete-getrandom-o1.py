class RandomizedSet:

    def __init__(self):
        self.posDict={}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.posDict.keys():
            return False
        self.arr.append(val)
        self.posDict[val] = len(self.arr)-1
        return True

    def remove(self, val: int) -> bool:
        ## swap the element from the back
        ## remove it from the back(len(arr)-1)
        if val not in self.posDict.keys():
            return False
        
        valpos = self.posDict[val] ##give this to last
        self.arr[valpos] = self.arr[-1]
        self.posDict[self.arr[-1]] = valpos
        self.arr[-1] = val
            
        del self.posDict[val]
        self.arr.pop()
        return True
        
#         val: pos
#         lastval: lastpos  => len(arr)-1 
        
        

    def getRandom(self) -> int:
        return random.choice(self.arr)
        # return self.arr[randompos]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()