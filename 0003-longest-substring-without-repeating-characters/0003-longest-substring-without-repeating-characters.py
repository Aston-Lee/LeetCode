# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
        
#         start = 0
#         charset = set()
#         maxLength = 0
#         # i = end
#         for i, char in enumerate (s):
#             if char not in charset:
#                 charset.add(char)
#                 maxLength = max(maxLength, len(charset))
#             else:
#                 while start <= i and s[start] != char:
#                     charset.remove(s[start])
#                     start += 1
#                 if s[start] == char:
#                     charset.remove(s[start])
#                     start += 1
#                 charset.add(char)
#         maxLength = max(maxLength, len(charset))
#         return maxLength
    
    
class Solution:    
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        maxLength = 0
        charIndexMap = {}
        
        for i, char in enumerate(s):
            if char in charIndexMap and charIndexMap[char] >= start:
                start = charIndexMap[char] + 1
            charIndexMap[char] = i
            maxLength = max(maxLength, i - start + 1)
        
        return maxLength