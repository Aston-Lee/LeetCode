class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # center, diameter
        ## check the updating logic
        
        if len(s) == 1:
            return s
        
        res = s[0]
        
        for i in range(len(s)):
            diameter = 0
            while i - diameter != -1 and i + diameter != len(s):
                if s[i - diameter] == s[i + diameter]:
                    diameter += 1
                else:
                    break
            if 2*diameter - 1 > len(res):
                res = s[i - diameter + 1 : i + diameter]
            
        for i in range(len(s)-1):
            diameter = 0
            if s[i] == s[i+1]:
                while i - diameter != -1 and i+1 + diameter != len(s):
                    if s[i - diameter] == s[i+1 + diameter]:
                        diameter += 1
                    else:
                        break
                if 2*diameter > len(res):
                    res = s[i - diameter + 1 : i+1 + diameter]
                    
        return res
        
        