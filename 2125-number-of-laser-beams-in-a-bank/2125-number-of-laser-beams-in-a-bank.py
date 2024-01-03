class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        '''
        ["011001","000000","010100","001000"]
        3 0 2 1
        l   r
        3*2 + 2*1    
        
        ans += 3*2 + 2*1
        ["000","111","000"]
        0 3 0
          l   r
    
        
        '''
        def add(s):
            tmp = 0
            for c in s:
                if c == '1':
                    tmp += 1
                    
            return tmp
        banksum = [add(b) for b in bank]
        l, r = 0, 1
        ans = 0
        while r < len(banksum):
            if banksum[l] and banksum[r]:
                ans += banksum[l] * banksum[r]
                l = r
                r = l+1
            elif banksum[l] and not banksum[r]:
                r += 1
            elif not banksum[l] and banksum[r]:
                l = r
                r = l+1
            else:
                l += 1
                r += 1
                
        return ans 
        