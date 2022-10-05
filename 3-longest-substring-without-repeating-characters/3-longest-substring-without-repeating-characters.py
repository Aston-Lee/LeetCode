class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # @sliding window + 2 pointer Time:O(n) Space: O(1)
        l, r = 0, 0
        charSet = set()
        res = 0
        while r!=len(s):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            res = max(res, r-l+1)
            r+=1
        return res