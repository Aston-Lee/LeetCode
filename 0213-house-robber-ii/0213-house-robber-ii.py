class Solution:
    def rob(self, nums: List[int]) -> int:
        # cant robe geginning and the last
        # so seperate two proportion and do regular dp
        
        
        def dp(nums):
            mem = [False] * len(nums)
            if len(nums) >= 1:
                mem[0] = nums[0]
            if len(nums) >= 2:
                mem[1] = nums[1]
            if len(nums) == 2:
                return max(mem[:2])
            for i in range(2, len(nums)):
                mem[i] = nums[i] + max(mem[i-2], mem[i-3])
            if len(mem) >= 2:
                return max(mem[-1], mem[-2])
            else:
                return mem[-1]

        
        def helper(nums):
            if len(nums) == 1:
                return nums[0]
            else:
                return max(dp(nums[:-1]), dp(nums[1:]))
        
        return helper(nums)
        
        
        