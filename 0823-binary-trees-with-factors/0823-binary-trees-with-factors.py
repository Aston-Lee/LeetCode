class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr = sorted(arr)
        dp = [1]*len(arr)
        
        ValPos = {}
        for i, num in enumerate(arr):
            ValPos[num] = i
            
        for num in arr:
            for j in arr:
                if j >= num:
                    break
                # j is the leftnode, num/j is the rightnode
                if num%j == 0 and num/j in ValPos.keys() : 
                    dp[ValPos[num]] += dp[ValPos[j]]*dp[ValPos[int(num/j)]]
                
        return sum(dp) % 1000000007
            
            