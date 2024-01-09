class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        piles = [3,6,7,11], h = 8
        minK = 1, maxK = max(piles)
        bs(l=1, r=11)
        
        '''
        l, r = 1, max(piles)
        while l <= r:
            # print(l, r)
            mid = (l+r)//2
            time = 0
            for p in piles:
                time += math.ceil(p/mid)
            if time == h:
                k = mid
                tmp = h
                while tmp == h:
                    k -= 1
                    if k == 0:
                        return 1
                    tmp = 0
                    for p in piles:
                        tmp += math.ceil(p/k)
                return k + 1
            elif time > h: # k too small
                l = mid + 1
            else: # time < h
                r = mid - 1
                
        return l