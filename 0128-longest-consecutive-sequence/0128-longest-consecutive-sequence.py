class Solution:
    def longestConsecutive(self, nums):
        
        if nums == []:
            return 0
        
        numSet = set(nums)
        maxLength = 1
        for n in nums:
            if n+1 in numSet and n-1 not in numSet:
                cur = n
                tmpLength = 1
                while cur+1 in numSet:
                    cur = cur+1
                    tmpLength += 1
                maxLength = max(maxLength, tmpLength)
        
        return maxLength