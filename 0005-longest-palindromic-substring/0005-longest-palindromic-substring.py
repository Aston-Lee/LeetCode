class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        
        longest = -float('inf')
        ans = []
        #check single 
        for p in range(len(s)):
            l, r = p, p
            while 0 <= l and r < len(s):
                
                if s[l] == s[r]:
                    
                    if longest < r-l+1:
                        longest = r-l+1
                        ans = [l,r]
                else:
                    break
                l-=1
                r+=1
                
        #check double 
        for p in range(len(s)-1):
            l, r = p, p+1
            # print('---')
            while 0 <= l and r < len(s):
                if s[l] == s[r]:
                    # print(l, r, s[l], s[r])
                    if longest < r-l+1:
                        longest = r-l+1
                        ans = [l,r]
                else:
                    break
                l-=1
                r+=1
                
        return s[ans[0]:ans[1]+1]