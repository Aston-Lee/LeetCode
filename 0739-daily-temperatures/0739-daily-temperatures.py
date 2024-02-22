class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        '''
        monostack / only store smaller tmp 
        
        store [tmp, index]        
        '''
        
        stack = []
        res = [0] * len(temperatures)
        for i, tmp in enumerate(temperatures):
            if not stack:
                stack.append([tmp, i])
            elif stack and tmp < stack[-1][0]:
                stack.append([tmp, i])
            else:
                while stack and tmp > stack[-1][0]:
                    _ , index = stack.pop()
                    res[index] = i-index
                stack.append([tmp, i])
                
        return res