class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        ## dp solution O(n^2)/ O(n)
        dp = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(0,i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        
        return max(dp)
        