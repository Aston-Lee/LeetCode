class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
#         neighbor = [(1,0), (1,1), (0,1)]
        
#         ## dfs & dp
#         def dfs(i, j):
#             if 0<=i<m and 0<=j<n:
#                 return min(dfs(i,j+1), dfs(i+1, j+1), dfs(i+, j))

        rows, cols = len(matrix), len(matrix[0]) if len(matrix) > 0 else 0
        dp = [0] * (cols + 1)
        maxsqlen, prev = 0, 0
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                temp = dp[j]
                if matrix[i - 1][j - 1] == '1':
                    dp[j] = min(min(dp[j - 1], prev), dp[j]) + 1
                    maxsqlen = max(maxsqlen, dp[j])
                else:
                    dp[j] = 0
                prev = temp
        return maxsqlen * maxsqlen
        