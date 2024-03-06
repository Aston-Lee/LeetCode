class Solution:
    def reverse(self, x: int) -> int:
        
        positive = 1
        
        if x < 0:
            positive = -1
            x = -x
        
        ans = int(str(x)[::-1]) * positive 
        
        if not (- 2**31 <= ans <= 2**31 - 1):
            return 0
        else:
            return ans 