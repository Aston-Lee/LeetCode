class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#         if len(nums) == 1:
#             return nums[0]
    
#         nums = sorted(nums)
#         if nums[0] != nums[1]:
#             return nums[0]
#         elif nums[len(nums)-2] != nums[len(nums)-1]:
#             return nums[len(nums)-1]
#         for i in range(1,len(nums)-1):
#             if nums[i-1] != nums[i] and nums[i] != nums[i+1]:
#                 return nums[i]

        if len(nums) == 1: return nums[0]
        
        nums = sorted(nums)
        if len(nums)%2 == 1:
            for i in range(0, len(nums)-1, 2):
                if nums[i]!= nums[i+1]:
                    return nums[i]
            return nums[len(nums)-1]
        else:
            for i in range(0, len(nums), 2):
                if nums[i]!= nums[i+1]:
                    return nums[i]