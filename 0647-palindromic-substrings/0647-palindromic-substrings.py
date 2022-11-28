class Solution:
    def countSubstrings(self, s: str) -> int:
        #brute force 
        
#         abba
          
#         a b bb abba b a
        
#         a a b b bb abba
         
        
#         res = 
        
        # res = []
        counter = 0        
        for i in range(len(s)):
            
            ## odd
            l , r = i, i
            while 0<=l and r<len(s):
                if s[l] == s[r]:
                    # res.append(s[l:r+1])
                    counter += 1
                else:
                    break
                
                l-=1
                r+=1
            
            ## even
            l , r = i, i+1
            while 0<=l and r<len(s):
                if s[l] == s[r]:
                    # res.append(s[l:r+1])
                    counter += 1
                else:
                    break
                
                l-=1
                r+=1
                
        return counter