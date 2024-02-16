class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        char = set()
        longest = 0
        for r in range(len(s)):
            
            if s[r] in char:
                while l<r and s[l] != s[r]:
                    char.remove(s[l])
                    l += 1
                l += 1
            else:
                char.add(s[r])
                longest = max(r-l+1, longest)
            
            # print(l, r, s[r], char)
        
        return longest
        