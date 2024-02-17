class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        charSet = set()
        l = 0
        longest = 0

        for r in range(len(s)):
            # If the character is in the set, remove the leftmost character until it's not.
            # This eliminates the need for an inner while loop checking for inequality.
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            
            # Add the current character to the set and update the longest substring length if needed.
            charSet.add(s[r])
            longest = max(longest, r - l + 1)
        
        return longest
        
        
#         '''
#         for loop, 2 pointers
#         use set to record characters
#         while l<r and s[l] != s[r], charSet remove s[l], l+=1
#         and after while loop, l += 1
#         '''
#         l = 0
#         char = set()
#         longest = 0
#         for r in range(len(s)):
            
#             if s[r] in char:
#                 while l<r and s[l] != s[r]:
#                     char.remove(s[l])
#                     l += 1
#                 l += 1 ## because we stopped at s[l] == s[r] so after we found this l, l+= 1(since we didn't add s[r] into the set so we don't actually remove it )
#             else:
#                 char.add(s[r])
#                 longest = max(r-l+1, longest)
            
#             # print(l, r, s[r], char)
        
#         return longest
        