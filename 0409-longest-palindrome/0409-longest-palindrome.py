class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        '''
        only one single, or all double
        '''
        
        freq = collections.Counter(s)
        singleInferno = []
        
        ans = 0
        for key, val in freq.items():
            if val % 2 :
                singleInferno.append(val)
            else:
                ans += val
                
            
        foundMax = False 
        if singleInferno:
            for num in singleInferno:
                if not foundMax:
                    ans += num
                    foundMax = True 
                else:
                    ans += num-1
        
        return ans 
        
            
                