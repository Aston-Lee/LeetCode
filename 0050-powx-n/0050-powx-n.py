class Solution:
    def myPow(self, x: float, n: int) -> float:
        
#         @cache
#         def fastpow(x, w):
#             if w == 0:
#                 return 1
            
#             if w%2:
#                 return x* fastpow(x, w//2) * fastpow(x, w//2)
#             else:
#                 return fastpow(x, w//2) * fastpow(x, w//2)

        def fastpow(x, n):
            if x == 0: 
                return 0
            if n==1:
                return x
            res = fastpow(x * x, n // 2)
            return x * res if n % 2 else res
        
        
        if n < 0:
            n = -n
            x = 1/x
        
        if n == 0:
            return 1

        return fastpow(x, n)