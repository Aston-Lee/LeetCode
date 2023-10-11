class Solution:
    def trap(self, height: List[int]) -> int:
        
        ## left right scan solve
        leftscan, rightscan = [], []
        
        highest = 0
        for h in height:
            highest = max(highest, h)
            leftscan.append(highest)
            
        highest = 0
        height = height[::-1]
        for h in height:
            highest = max(highest, h)
            rightscan.append(highest)
        
        height = height[::-1] 
        rightscan = rightscan[::-1]
        
        res = 0
        for i in range(len(height)):
            res += min(leftscan[i], rightscan[i])-height[i]
            
        return res
        
        ## what is the 2 pointer way to solve this?
        