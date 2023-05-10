class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        monoStack = []
        res = [0]*len(temperatures)
        for i, tmp in enumerate(temperatures):
            while monoStack and tmp > monoStack[-1][0]:
                res[monoStack[-1][1]] = i - monoStack[-1][1]
                monoStack.pop()
    
            monoStack.append((tmp, i))
        return res 
        