class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        sfrequency = collections.Counter(s)
        tfrequency = collections.Counter(t)
        
        for key, val in tfrequency.items():
            if val != sfrequency[key]:
                return key
        
            
            