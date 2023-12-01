class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        ## try 2 pointer 
        ## "babad"
        longest = -float('inf')
        for p in range(len(s)):
            d = 0
            while 0 <= p-d and p+d < len(s):
                if s[p-d] != s[p+d]:
                    break
                d += 1
            d -= 1
            if 2*d+1 > longest:
                longest = 2*d+1
                ans = [p-d, p+d]

        ## "babbad", "cbbd"
        for p in range(len(s)-1):
            p1, p2 = p, p+1
            d = 0
            while 0 <= p1-d and p2+d < len(s):
                if s[p1-d] != s[p2+d]:
                    break
                d += 1
            d -= 1
            if 2*d+2 > longest:
                longest = 2*d+2
                ans = [p1-d, p2+d]
        
        return s[ans[0]: ans[1]+1]
        
#         n = len(s)
#         dp = [[False] * n for _ in range(n)]
#         ans = [0, 0]
        
#         for i in range(n):
#             dp[i][i] = True
        
#         for i in range(n - 1):
#             if s[i] == s[i + 1]:
#                 dp[i][i + 1] = True
#                 ans = [i, i + 1]

#         for diff in range(2, n):
#             for i in range(n - diff):
#                 j = i + diff
#                 if s[i] == s[j] and dp[i + 1][j - 1]:
#                     dp[i][j] = True
#                     ans = [i, j]

#         i, j = ans
#         return s[i:j + 1]