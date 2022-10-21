class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        ## stack, start from back
        ## logic
        ## if element is bigger than stack[-1], pop the stack and set res to position difference, and push itself
        ## if element is <= than stack[-1], push [pos, tmp] into the stack
        
        ## edge case 
        ## position 0, normal
        ## position -1, result always 0, use the last one to help position -2
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
                
            
        