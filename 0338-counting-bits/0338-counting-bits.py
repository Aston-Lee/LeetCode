class Solution:
    def countBits(self, n: int) -> List[int]:
        
        ans = []
        for i in range(n+1):
            tmp =  bin(i)[2:] 
            ones = 0
            for c in tmp:
                if c == '1':
                    ones += 1
            ans.append(ones)
                    
        return ans