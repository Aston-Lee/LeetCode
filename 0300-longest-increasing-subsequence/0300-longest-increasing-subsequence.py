class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
#         7 7 7 7 7 7 7
#         1 1 1 1 1 1 1
#           i
#         j
        
        LIS = [1]*len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    LIS[i] = max(LIS[j]+1, LIS[i])
        return max(LIS)