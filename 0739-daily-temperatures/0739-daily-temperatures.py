class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tmp = temperatures
        
        stack = []
        res = [0]*len(tmp)
        for i in range(len(tmp)):
            if len(stack)==0 or tmp[i] <= stack[-1][1]:
                stack.append([i, tmp[i]])
            else:
                while stack and tmp[i] > stack[-1][1]:
                    pos, pre_tmp = stack.pop()
                    res[pos] = i-pos
                stack.append([i,tmp[i]])
        
        return res