class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ## my idea hehe
        
        # s = "DEADOBECODEBANC", t = "ABC"
          
        if len(s) < len(t):
            return ""
        
        UpperArr = [0]*26
        LowerArr = [0]*26
        tSet = set(t)
        freqdict = Counter(t)
        
        l, r = None, None
        for i, char in enumerate(s):
            if char in tSet:
                l, r = i, i
                break
                
        if l == None: 
            return ""

        for key, value in freqdict.items():
            if key.isupper():
                UpperArr[ord(key)-ord('A')] = value
            else:
                LowerArr[ord(key)-ord('a')] = value
                
        if s[l].isupper():
            UpperArr[ord(s[l])-ord('A')] -= 1
        elif s[l] in tSet and not s[l].isupper():
            LowerArr[ord(s[l])-ord('a')] -= 1
        
                
        # "DE, ADOBECODEBANC" "ABC"
        #               l  r
        
        minLen = float('INF')
        tmpres = [None, None]
        res = ""
                
        while l<=len(s) and r <= len(s):
            # print(s[r], UpperArr)
            if max(UpperArr) > 0 or max(LowerArr) > 0:
                r+=1
                if r == len(s):
                    break
                if s[r] in tSet and s[r].isupper():
                    UpperArr[ord(s[r])-ord('A')] -= 1
                elif s[r] in tSet and not s[r].isupper():
                    LowerArr[ord(s[r])-ord('a')] -= 1
            else:
                if minLen > r-l+1:
                    minLen = r-l+1
                    tmpres = [l,r]
                
                # print(s[l])
                if s[l].isupper():
                    UpperArr[ord(s[l])-ord('A')] += 1
                elif s[l] in tSet and not s[l].isupper():
                    LowerArr[ord(s[l])-ord('a')] += 1
                l+=1
                if l == len(s):
                    break
                    
                while l!=len(s) and s[l] not in tSet:
                    # print("s[l]:", s[l])
                    l += 1
                
                if l == len(s):
                    break
        if tmpres == [None, None]:
            return ""
        else:
            return s[tmpres[0]: tmpres[1]+1]
