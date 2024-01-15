class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        ans = 0
        index = {}
        for i, char in enumerate(keyboard):
            index[char] = i
            
        prev = 0
        for w in word:
            ans += abs(index[w]-prev)
            prev = index[w]
        
        return ans