class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def fastPow(x, n):
            if x == 0: 
                return 0
            if n==1:
                return x
            res = fastPow(x * x, n // 2)
            return x * res if n % 2 else res
            
            
        if n < 0:
            x = 1/x
            n = -n
        if n == 0:
            return 1
        
        return fastPow(x, n)