class TimeMap:

    def __init__(self):
        self.myDict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key not in self.myDict.keys() :
            self.myDict[key] = [[timestamp, value]]
        else:
            self.myDict[key].append([timestamp, value])
            
        # print(self.myDict)

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.myDict.keys():
            return ""
        else:
            if timestamp < self.myDict[key][0][0]:
                return ""
            elif timestamp >= self.myDict[key][-1][0]:
                return self.myDict[key][-1][1]
            else:
                ## optimize. Binary Search
                left = 0
                right = len(self.myDict[key])-1
                
                while left < right:
                    mid = (left + right) // 2
                    if self.myDict[key][mid][0] <= timestamp and self.myDict[key][mid+1][0] > timestamp:
                        return self.myDict[key][mid][1]
                    elif self.myDict[key][mid][0] > timestamp and timestamp > self.myDict[key][left][0]:
                        right = mid
                    elif self.myDict[key][mid][0] < timestamp and timestamp < self.myDict[key][right][0]:
                        left = mid
                
                
                # ## brute force. loop through
                # for i in range(len(self.myDict[key])-1):
                #     if self.myDict[key][i][0] <= timestamp and timestamp < self.myDict[key][i+1][0]:
                #         return self.myDict[key][i][1]
                
                

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)