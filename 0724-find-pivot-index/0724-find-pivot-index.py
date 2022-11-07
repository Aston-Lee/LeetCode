class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        rsum = 0
        for n in nums:
            rsum += n
        
        lsum = 0
        for i, n in enumerate(nums):
            if i == 0:
                rsum -= n
                if lsum == rsum:
                    return i
                continue
            lsum += nums[i-1]
            rsum -= n
            if lsum == rsum:
                return i
        
        return -1