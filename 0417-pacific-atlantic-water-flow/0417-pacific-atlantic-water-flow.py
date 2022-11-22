class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        
        pacific_queue = deque()
        atlantic_queue = deque()
        for i in range(m):
            pacific_queue.append((i, 0))
            atlantic_queue.append((i, n-1))
        
        for j in range(n):
            pacific_queue.append((0, j))
            atlantic_queue.append((m-1, j))
            
            
        def bfs( queue ):
            reachable = set()
            while queue: 
                row, col = queue.popleft()
                reachable.add((row, col))
                for (x,y) in [(1,0), (-1,0), (0,1), (0,-1)]:
                    new_row, new_col = row+x, col+y
                    if new_row < 0 or new_col<0 or new_row >= m or new_col >= n:
                        continue
                    if (new_row, new_col) in reachable:
                        continue
                    
                    ## current reachable, 
                    ## if land inside is lower, no need to add it io the queue
                    if matrix[new_row][new_col] < matrix[row][col]:
                        continue
                    queue.append((new_row, new_col))

            return reachable
            
        
        pacific_reachable = bfs(pacific_queue)
        atlantic_reachable = bfs(atlantic_queue)
        
        # return list(pacific_reachable.intersection(atlantic_reachable))
        return list(pacific_reachable & atlantic_reachable)