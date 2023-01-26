class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        res = []
        seen = set(nums)
        for i in range(1, len(nums)+1):
            if i not in seen:
                res.append(i)
                
        return res