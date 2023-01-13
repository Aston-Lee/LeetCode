class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        remain = {}
        for i, val in enumerate(nums):
            remain[target - val] = i
            
        for i, val in enumerate(nums):
            if val in remain and  i!= remain[val]:
                
                return [i, remain[val]]