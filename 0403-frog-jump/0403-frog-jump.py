from heapq import heappop, heappush, heappushpop

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        '''
        If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units. The frog can only jump in the forward direction.
        stones = [0,1,3,5,6,8,12,17]
        0 + 1, unit = 1
        1 + 1 not in set unit = 1
        1 + 2 in set, unit = 2
        
        3 + 1 not in set
        3 + 2 in set, unit = 2
        3 + 3 in set, unit = 3
        
        5 + 1 in unit = 1
        5 + 2 not in
        5 + 3 in unit = 3
        
        6 + 2 in unit = 2
        6 + 3 not in
        6 + 4 not in
        
        6 + 1 not in
        6 + 2 in unit = 2
        
        8 + 2 not in
        8 + 3 not in
        8 + 4 in
        
        optimal is to add k+1 to k-1
        or use dp to store (stones, unit) in a set to know if we have run this before
        use bfs, or simply a while loop
        '''
        target = stones[-1]
        visited = set()
        heap = []
        heappush(heap, (0,0))
        candidate = set(stones)
        while heap:
            stone, unit = heappop(heap) 
            # print(stone, unit)
            if stone == target:
                return True
            
            for u in range(unit-1, unit+2):
                if u < 1:
                    continue
                if stone + u in candidate and (stone + u, u) not in visited:
                    visited.add((stone + u, u))
                    heappush(heap, (stone + u, u))
        
        return False