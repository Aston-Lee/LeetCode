class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # freq = collections.Counter(nums)
        freq = {}
        for n in nums:
            if n in freq.keys():
                freq[n] += 1
            else:
                freq[n] = 1
        n = len(nums)/2
        for i in freq:
            if freq[i] > n:
                return i