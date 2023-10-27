class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        
        # babad
        # lcr
        # c = 1
        # d = 0
        ## single
        res = [-float('inf'), [None, None]]
        for c in range(len(s)):
            d = 0
            l, r = c, c
            while True:
                l, r = c-d, c+d
                if not (0 <= l) or not (r < len(s)) or (s[l] != s[r]):
                    break
                if (r-l+1 > res[0]):
                    res = [r-l+1, [l, r]]
                d += 1
    
        ## double
        for c in range(len(s)-1):
            d = 0
            l, r = c, c+1
            while True:
                l, r = c-d, c+1+d
                # print(l, r, d)
                if not (0 <= l) or not (r < len(s)) or (s[l] != s[r]):
                    break
                if (r-l+1 > res[0]):
                    res = [r-l+1, [l, r]]
                d += 1
                
        return s[res[1][0]:res[1][1]+1]
        
        
        
          
        