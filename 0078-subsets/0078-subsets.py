class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        res = []
        for i in range(2**n, 2**(n+1)):
            bitmap = bin(i)[3:]
            res.append([ nums[j] for j in range(n) if bitmap[j]=='1'])
            
        return res
            