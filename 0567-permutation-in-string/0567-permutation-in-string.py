class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        ## Brute Force Solution 
        s1freq = Counter(s1)
        s2freq = Counter(s2)
        s1set = set(s1)
        
        for key, val in s1freq.items():
            if s2freq[key] < val:
                return False
            
        for i, c in enumerate(s2):
            if c in s1set:
                tmpfreq = defaultdict(int)
                for j in range(len(s1)):
                    if i+j >= len(s2):
                        return False
                    tmpfreq[s2[i+j]] += 1
                    if tmpfreq[s2[i+j]] > s1freq[s2[i+j]]:
                        break
                if tmpfreq == s1freq:
                    return True
                
        return False