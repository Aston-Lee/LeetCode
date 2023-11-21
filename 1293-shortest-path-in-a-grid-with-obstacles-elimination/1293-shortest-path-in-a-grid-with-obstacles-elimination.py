class Solution:
    def __init__(self):
        self.minT = float('inf')
    
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
#         '''
#         dfs
#         '''
#         tobreak = 0
#         for g in grid:
#             tobreak += sum(g)
#         print(tobreak)
        
#         if k < tobreak:
            
#             NEI = [(1,0), (-1,0), (0,1), (0,-1)]
#             m, n = len(grid), len(grid[0])
#             visited = set()


#             def dfs(i, j, t, remain_k):
#                 if (i,j) == (m-1, n-1):
#                     self.minT = min(self.minT, t)
#                 if (i,j) in visited:
#                     return
#                 visited.add((i,j))
#                 for _x, _y in NEI:
#                     ni, nj = i+_x, j+_y
#                     if 0<=ni<m and 0<=nj<n and (ni, nj) not in visited:
#                         if grid[ni][nj]==0:
#                             dfs(ni, nj, t+1, remain_k)
#                         elif grid[ni][nj]==1 and remain_k:
#                             # tmpvisited = visited
#                             dfs(ni, nj, t+1, remain_k-1)
#                             # visited = tmpvisited

#             dfs(0, 0, 0, k)
#             return self.minT if self.minT != float('inf') else -1
            
#         else:
        
        '''
        bfs

        '''
        NEI = [(1,0), (-1,0), (0,1), (0,-1)]
        m, n = len(grid), len(grid[0])

        dq = deque()
        dq.append((0,0,0,k))
        visited = set()
        visited.add((0,0,k))
        while dq:
            for _ in range(len(dq)):
                (step, i, j, remain) = dq.popleft()
                if (i, j) == (m-1, n-1):
                    return step
                for _x, _y in NEI:
                    ni, nj = i+_x, j+_y
                    if 0<=ni<m and 0<=nj<n:
                        new_remain = remain-grid[ni][nj]
                        if (ni, nj, new_remain) not in visited and new_remain >= 0:
                            visited.add((ni, nj, new_remain))
                            dq.append((step+1, ni, nj, new_remain))

        return -1