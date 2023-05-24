class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        firstSet = set()     
        secondSet = set()
        
        for n in nums:
            if n not in firstSet:
                firstSet.add(n)
            elif n in firstSet:
                secondSet.add(n)
                
        return list(secondSet).pop()
        
        