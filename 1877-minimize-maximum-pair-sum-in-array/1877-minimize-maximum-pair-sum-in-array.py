class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        
        nums.sort()
        n = len(nums) #6
        small = nums[:n//2]
        large = nums[n//2:][::-1]
        
        maxPairSum = -float('inf')
        for i in range(n//2):
            maxPairSum = max(maxPairSum, small[i]+large[i])
        
        return maxPairSum
    
        
        