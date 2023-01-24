class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        
        m = p/math.gcd(p,q)
        n = q/math.gcd(p,q)
        
        m = m%2
        n = n%2
        
        if (m,n) == (1,0):
            return 0
        elif (m,n) == (1,1):
            return 1
        elif (m,n) == (0,1):
            return 2
        else:
            return 3