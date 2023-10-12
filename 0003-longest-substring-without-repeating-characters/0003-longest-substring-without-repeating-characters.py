class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        showed = set()
        length = 0
        l = 0
        for r, c in enumerate(s):
            if c in showed:
                while s[l] != c:
                    showed.remove(s[l])
                    l+=1
                l+=1  
                
            else:
                showed.add(c)
            length = max(length, r-l+1)
        
        length = max(len(s)-1-l+1, length)
        return length
    
#         s = "pwwkew"
#         Solution.lengthOfLongestSubstring(s)