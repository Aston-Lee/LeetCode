class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        def getbits(num) -> int: # return how many bits for this num
            return sum( int(bit) for bit in bin(num)[2:])
          
        minheap = []
        for num in arr:
            heappush(minheap,  (getbits(num), num))
            
        result = []
        while minheap:
            result.append(heappop(minheap)[1])
            
        return result
            
            
        