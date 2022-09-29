class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i, n in enumerate(nums):
            if target-n in hashmap.keys():   
                return [i, hashmap[target-n]]
            else:
                hashmap[n] = i