class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ## thinking from the back if the back can reach to front wiil be O(n^2)
        
        ## 2 pointer, O(n)
        target = len(nums)-1
        l, r = 0, 0
        while(l<r+1):
            if r >= target:
                return True
            if l + nums[l] > r:
                r = l + nums[l]
            if l == r and nums[l] == 0:
                return False
            l += 1
        
        
        