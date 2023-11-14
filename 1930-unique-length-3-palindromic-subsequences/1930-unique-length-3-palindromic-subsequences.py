class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
        candidate = set(s)
        res = 0
        for char in candidate:
            l = s.index(char)
            r = s.rindex(char)
            tmpset = set()
            for i in range(l+1, r):
                if s[i] not in tmpset:
                    tmpset.add(s[i])
                    res += 1
        
        return res 
        