class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        
        n = len(words)
        
        count = defaultdict(int)
        for word in words:
            for char in word:
                count[char] += 1
            
        for key, val in count.items():
            if val % n:
                return False
            
        return True
            