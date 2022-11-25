class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = [0 ,0]
        globallen = 0
        for i in range(len(s)):
            locallen = 0
            ## odd, eg "bab"
            l, r = i, i
            while 0 <= l and r < len(s):
                if s[l] == s[r]:
                    locallen = r - l + 1
                    if locallen > globallen:
                        globallen = locallen
                        res = [l, r]
                else:
                    break
                l -= 1
                r += 1
                
            ## even
            l, r = i, i+1
            while 0 <= l and r < len(s):
                if s[l] == s[r]:
                    locallen = r - l + 1
                    if locallen > globallen:
                        globallen = locallen
                        res = [l, r]
                else:
                    break
                l -= 1
                r += 1
        
        return s[res[0]:res[1]+1]