class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        def checking(short, long):
            
            targetDict = collections.Counter(short)
            currDict = defaultdict(int)
            
            l = 0
            for r in range(len(long)):
                currDict[long[r]] += 1
                if targetDict == currDict:
                    return True
                
                while currDict[long[r]] > targetDict[long[r]]:
                    currDict[long[l]] -= 1
                    if currDict[long[l]] == 0:
                        del currDict[long[l]]
                    l += 1
                    if l>r:
                        break
            return targetDict == currDict
                
        return checking(s1, s2) if len(s1) <= len(s2) else False
        