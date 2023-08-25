class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
#         N = len(grid)-1
#         minHeap = [(grid[0][0], 0, 0)]
#         visit = set()
#         direction = [(1,0), (0,1), (-1,0), (0,-1)]
        
#         while minHeap:
#             t, i, j = heapq.heappop(minHeap)
#             visit.add((i,j))
#             if i == N and j == N:
#                 return t
#             for di, dj in direction:
#                 ni, nj = i+di, j+dj
#                 if  0 > ni or \
#                     0 > nj or \
#                     ni > N or \
#                     nj > N or \
#                     (ni, nj) in visit:
#                         continue
#                 heapq.heappush(minHeap, (max(t, grid[ni][nj]), ni, nj))
                
        N = len(grid)
        visit = set()
        minH = [[grid[0][0], 0, 0]]  # (time/max-height, r, c)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        visit.add((0, 0))
        while minH:
            t, r, c = heapq.heappop(minH)
            if r == N - 1 and c == N - 1:
                return t
            for dr, dc in directions:
                neiR, neiC = r + dr, c + dc
                if (
                    neiR < 0
                    or neiC < 0
                    or neiR == N
                    or neiC == N
                    or (neiR, neiC) in visit
                ):
                    continue
                visit.add((neiR, neiC))
                heapq.heappush(minH, [max(t, grid[neiR][neiC]), neiR, neiC])