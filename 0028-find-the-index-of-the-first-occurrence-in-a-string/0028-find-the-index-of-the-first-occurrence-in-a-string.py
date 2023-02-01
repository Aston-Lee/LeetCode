class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        # optimize: prefixtree on haystack
        
        ## brute force O(n^2)
        if len(haystack) < len(needle):
            return -1
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                found = True
                for j in range(len(needle)):
                    if i+j > len(haystack)-1:
                        return -1
                    if needle[j] != haystack[i+j]:
                        found = False
                        break
                if found:
                    return i
            
        return -1
