class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = collections.defaultdict(list) ## note collections.defaultdict(list)
        for word in strs:
            count = [0]*26
            for char in word:
                count[ord(char)-ord('a')] += 1
            ans[tuple(count)].append(word)
            
        return ans.values()