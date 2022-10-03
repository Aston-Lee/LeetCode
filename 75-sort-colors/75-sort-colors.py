class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #in place
        s = sorted(nums)
        for i, n in enumerate(nums):
            nums[i] = s[i]
        