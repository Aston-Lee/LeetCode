class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = collections.Counter(nums)
        n = len(nums)/2
        for i in freq:
            if freq[i] > n:
                return i