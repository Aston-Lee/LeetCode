class Solution:
    def reverseBits(self, n: int) -> int:
#         print(str(bin(n)[2:].zfill(32))[::-1])
#         print(int(str(bin(n)[2:].zfill(32))[::-1], 2))
#         print('----')
        
        return int(str(bin(n)[2:].zfill(32))[::-1], 2)