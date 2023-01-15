class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
       
        freqdict = Counter(t)
        l, r = 0, 0
        minLen = float('INF')
        res = ""
        count = defaultdict(int)
        
        while r < len(s):
            if s[r] in freqdict:
                count[s[r]] += 1
            while all(count[c] >= freqdict[c] for c in freqdict):
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    res = s[l:r+1]
                if s[l] in freqdict:
                    count[s[l]] -= 1
                l += 1
            r += 1
        return res
