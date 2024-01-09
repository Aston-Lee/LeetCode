class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        s = "AABABBA", k = 1
             l   r
        
        A : 3
        b : 2
        length : 5
        length-max(dict.items()[1]) <= k
            while length-max(dict.items()[1]) > k:
                l += 1
                dict[s[l]] -= 1
        maxlength : 4
        
        
        '''
        l, r = 0, 0
        maxlength = 0
        freq = defaultdict(int)
        while r < len(s):
            # print(l, r, s[r])
            freq[s[r]] += 1
            while r-l+1-max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1
            length = r-l+1
            maxlength = max( maxlength, length )
            r += 1
        return maxlength 