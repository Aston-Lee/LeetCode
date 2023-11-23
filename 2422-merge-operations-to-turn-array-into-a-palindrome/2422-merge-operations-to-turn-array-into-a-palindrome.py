class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        l, r = 0, len(nums)-1
        time = 0
        while l < r:
            if nums[l] == nums[r]:
                l += 1
                r -= 1
                continue
            time += 1
            if nums[l] > nums[r]:
                right = nums[r]
                # nums = nums[0:r] + nums[r+1:]
                r -= 1
                nums[r] += right
            else:
                left = nums[l]     
                # nums = nums[0:l] + nums[l+1:] 
                l += 1
                nums[l] += left 
        return time 
        
        
        
        
        
          