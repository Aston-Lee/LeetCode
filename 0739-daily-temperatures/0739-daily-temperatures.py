class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        '''
        monostack: store index instead of temperatures
        
        '''
        stack = []
        n = len(temperatures)
        ans = [0]*len(temperatures)
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                ans[index] = i-index
            stack.append(i)

        return ans 
        
        
        
        
        