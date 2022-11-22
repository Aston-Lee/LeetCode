class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        
        tmp = 1
        group = []
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                group.append(tmp)
                tmp = 1 
            else:
                tmp+=1
        group.append(tmp)
                
        print(group)
                
        res = 0     
        for i in range(1, len(group)):
            res += min(group[i-1], group[i])
        
        return res