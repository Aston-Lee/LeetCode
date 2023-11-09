class Solution:
    def countHomogenous(self, s: str) -> int:
        
        MOD = 10**9 + 7
        
#         abbcccaa
#         dict = {
#             a : [0,0], [6,7]
#             b : [1,2]
#             c : [3,5]
#         }
            
#         [0]     res += i+1 for i in range(0-0+1) # res = 1
#         [6,7]   res += i+1 for i in range(7-6+1) # res = 4
#         [1,2]   res += i+1 for i in range(2-1+1) # res = 7
#         [3,5]   res += i+1 for i in range(5-3+1) # res = 13
         
        posdict = defaultdict(list)
        currchar = None
        start, end = None, None
        for i, char in enumerate(s):
            if currchar:
                if currchar != char:
                    posdict[currchar].append([start, i-1])
                    start, end = i, None
                    currchar = char
                else:
                    continue
            else:
                currchar = char
                start, end = i, None
                
        if end == None:
            posdict[currchar].append([start, len(s)-1])
        
        res = 0
        for char, lists in posdict.items():
            for s, e in lists:
                length = e-s+1 
                res += int((1+length)*(length)/2) % MOD
        return res % MOD
                
            