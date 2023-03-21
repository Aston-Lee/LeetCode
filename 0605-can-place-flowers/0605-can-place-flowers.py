class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        if flowerbed == [0]:
            return True
        
        currLen = 0
        available = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                currLen += 1
            else:
                if currLen != 0:
                    if i-currLen != 0:
                        available += (currLen-1)//2
                    else:
                        available += currLen//2
                currLen = 0
            
        if currLen != 0:
            available += currLen//2
            if currLen == len(flowerbed) and currLen%2 ==1:
                available += 1

                    
        return available >= n