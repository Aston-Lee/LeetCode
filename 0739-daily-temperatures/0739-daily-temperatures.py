class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        smallStack = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while smallStack and smallStack[-1][0] < t:
                tmp, pos = smallStack.pop()
                res[pos] = i - pos
            smallStack.append((t,i))
        return res
    
    
        
        