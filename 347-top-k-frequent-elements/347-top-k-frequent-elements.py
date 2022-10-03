class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freqdict = {}
        for n in nums:
            freqdict[n] = 1 + freqdict.get(n ,0) # this is a very neet technique
        
        # bucket sort idea
        freq = [ [] for i in range(len(nums)+1) ]
        for n, count in freqdict.items():
                freq[count].append(n)
        
        res = []
        for i in range(len(nums), 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) >= k:
                    return res
        
        