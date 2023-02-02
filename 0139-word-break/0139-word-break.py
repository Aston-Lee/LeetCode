class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wordSet = set(wordDict)
        dp = [False]*(len(s)+1)
        dp[0] = True
        
        for i in range(len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
        
        return dp[len(s)]
                    
        
        