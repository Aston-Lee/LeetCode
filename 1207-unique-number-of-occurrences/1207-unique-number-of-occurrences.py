class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        freqdict = collections.Counter(arr)
        freqset = set()
        for key, val in freqdict.items():
            if val in freqset:
                return False
            freqset.add(val)
        
        return True