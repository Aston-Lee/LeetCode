class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # @TLE
        pcount = [0]*26
        for i in range(len(p)):
            pcount[ord(p[i])-ord('a')] += 1
        
        output = []
        scount = [0]*26
        
            
        for i in range(len(s)):
            scount[ord(s[i])-ord('a')] += 1
            if i>=len(p):
                scount[ord(s[i-len(p)])-ord('a')] -= 1
            if pcount == scount:
                output.append(i-(len(p)-1))
        
        return output