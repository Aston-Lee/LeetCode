class Solution:
    def integerBreak(self, n: int) -> int:
        
        if n == 2:
            return 1
        elif n == 3:
            return 2
        
        def max3(k):
            return k//3
        
        arr = [3]*max3(n)
        if n%3:
            arr.append(n%3)
        
        if arr[-1] == 1:
            arr[-2], arr[-1] = 2, 2
        
        res = 1
        
        for num in arr:
            res *= num
            
        return res
        
        
        
        