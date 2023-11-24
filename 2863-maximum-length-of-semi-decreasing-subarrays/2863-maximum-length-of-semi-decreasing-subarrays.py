class Solution:
    def maxSubarrayLength(self, nums: List[int]) -> int:
        
        # dp 
        # stack 
        # queue
        # dfs 
        # bfs
        '''
        2pointer ## brute force, optimize only check of later is larger
        
        [57,55,50,60,61,58,63,59,64,60,63]
                     l                  r
                     
        [92,50]
       r    l
        '''
        l = 0
        maxlength = 0
        while l <= len(nums)-1:
            r = len(nums) - 1
            length = 0
            while l<=r and nums[l] <= nums[r]:
                r -= 1
            length = max(length, r-l+1)
            maxlength = max(maxlength, length)
            while l+1 < len(nums) and nums[l+1] <= nums[l]:
                l += 1
            l+=1
        return maxlength 
        
