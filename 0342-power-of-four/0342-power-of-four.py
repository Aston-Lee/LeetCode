class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1: return True
        if n == 0: return False
        if n < n:
            n = -n
        binary = bin(n)[2:]
        length = len(binary)
        print(binary, length)
        return int(binary[1:]) == 0 and (length-1)%2 == 0
        
        