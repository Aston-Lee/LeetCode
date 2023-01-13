class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # a = collections.Counter(nums)
        # for value in a.values():
        #     if value > 1: return True
        # return False
    
        nums_set = set(nums)
        return not (len(nums_set) == len(nums))
        
        # @dict TLE
        # mydict = {}
        # for n in nums:
        #     if n in mydict.keys():
        #         return True
        #     else:
        #         mydict[n] = False
        # return False