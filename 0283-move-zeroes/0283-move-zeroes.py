class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        [0,1,0,3,12]
        i = 0 [1,inf,3,12,inf]
        i = 1 [1,3,12,inf,inf] 
        
        """
            
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] == 0:
                    nums[i], nums[j] = nums[j], nums[i]
                    
        return nums