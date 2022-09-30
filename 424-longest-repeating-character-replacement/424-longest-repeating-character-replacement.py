class Solution(object):
    def characterReplacement(self, s, k):

        l = 0 
        freq = {}
        maxlen = 0
        for r in range(len(s)):
            if s[r] in freq.keys():
                freq[s[r]] +=1
            else:
                freq[s[r]] = 1
        
            currentlen = r - l + 1
            if currentlen - max(freq.values()) <= k :
                maxlen = max(maxlen, currentlen)
            else:
                freq[s[l]] -= 1
                l += 1
            # print(freq)
            
        return maxlen
        