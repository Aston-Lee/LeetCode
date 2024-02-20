class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
#         [2,0,2,1,1,0]
        
#         2 0 2 1 1 0
#         0 2 2 1 1 0
#         0 2 1 2 1 0
#         0 2 1 1 2 0
#         0 2 1 1 0 2
        
        
        ## @bubble sort
        for i in range(1, len(nums)):
            for j in range(0, len(nums)-1):
                if nums[j] > nums[i] :
                    nums[i], nums[j] = nums[j], nums[i]
        return nums
        
        ## @quick sort
        
        