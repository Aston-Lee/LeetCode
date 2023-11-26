class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        
#         path 
#         pattern 0,0 1,0 0,1 1,1
#         visited = actual 
#         dq 
#         area = 4
        
        
#         ansset.add(4, visited)

        NEI = [(1,0), (-1,0), (0,1), (0,-1)]

        m, n = len(grid), len(grid[0])
        
        def _check(base_i, base_j):
            dq = deque([(base_i, base_j)])
            pattern = [(0,0)]
            visited = set([(base_i, base_j)])
            area = 0
            while dq:
                for _ in range(len(dq)):
                    base_x, base_y = dq.popleft()
                    grid[base_x][base_y] = 0
                    area += 1
                    for _x, _y in NEI:
                        if 0 <= base_x+_x < m and 0 <= base_y+_y < n and grid[base_x+_x][base_y+_y] == 1 and (base_x+_x, base_y+_y) not in visited:
                            dq.append((base_x+_x, base_y+_y))
                            visited.add((base_x+_x, base_y+_y))
                            pattern.append((base_x+_x-base_i, base_y+_y-base_j))
                            
            return area, pattern
                            
        ans = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    a, patt = _check(i,j)
                    # print(a, patt)
                    ans.add((a, tuple(patt)))
                    
                    
        return len(ans)
        
        
    