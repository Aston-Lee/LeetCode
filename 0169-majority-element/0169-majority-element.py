class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # nums.sort()
        # return nums[len(nums)//2]
        
        maxVal = 0
        ans = None
        freq = collections.Counter(nums)
        for key, val in freq.items():
            if val > maxVal:
                maxVal = val
                ans = key
            
        return ans