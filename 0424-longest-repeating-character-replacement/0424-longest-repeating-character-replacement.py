class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # ## 2 pointer 
        # l, r = 0, 0
        # freqdict = {} 
        # maxlen = 0
        # addFlag = True 
        # while r != len(s):
        #     if addFlag == True:
        #         freqdict[s[r]] = freqdict.get(s[r], 0) + 1
        #     length = r - l + 1 
        #     if length - max(freqdict.values()) <= k:
        #         addFlag = True
        #         maxlen = max(maxlen, length)
        #         r += 1
        #     else:
        #         addFlag = False
        #         freqdict[s[l]] -= 1
        #         l += 1
        # return maxlen
        
        l = 0 
        freq = defaultdict(int)
        maxlen = 0
        for r in range(len(s)):
            freq[s[r]] +=1
            currentlen = r - l + 1
            if currentlen - max(freq.values()) <= k :
                maxlen = max(maxlen, currentlen)
            else:
                freq[s[l]] -= 1
                l += 1
            # print(freq)
            
        return maxlen
        