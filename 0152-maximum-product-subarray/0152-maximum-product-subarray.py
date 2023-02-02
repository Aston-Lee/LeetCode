class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0

        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far

        for i in range(1, len(nums)):
            curr = nums[i]
            temp_max = max(curr, max_so_far * curr, min_so_far * curr)
            temp_min = min(curr, max_so_far * curr, min_so_far * curr)
            
            max_so_far = temp_max
            min_so_far = temp_min

            result = max(max_so_far, result)

        return result