class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        @cache
        def fastpow(x, w):
            if w == 0:
                return 1
            
            if w%2:
                return x* fastpow(x, w//2) * fastpow(x, w//2)
            else:
                return fastpow(x, w//2) * fastpow(x, w//2)
        
        
        if n < 0:
            n = -n
            x = 1/x

        return fastpow(x, n)