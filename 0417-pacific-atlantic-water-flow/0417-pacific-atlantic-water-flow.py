class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        DIR = [(0,1), (0,-1), (1,0), (-1,0)]
        
        def bfs(queue):
            reachable = set()
            while queue:
                i, j = queue.pop()
                reachable.add((i,j))
                for x, y in DIR:
                    col, row = i+x, j+y
                    if not (0 <= col < m) or not (0 <= row < n):
                        continue
                    if (col,row) in reachable:
                        continue
                    if heights[col][row] < heights[i][j]:
                        continue
                    queue.append((col, row))
                    
            return reachable
        
        m, n = len(heights), len(heights[0])
        
        pacific, atlantic = deque(), deque()
        for i in range(m):
            pacific.append((i,0))
            atlantic.append((i,n-1))
            
        for i in range(n):
            pacific.append((0,i))
            atlantic.append((m-1,i))
            
        pacificReachable  = bfs(pacific)
        atlanticReachable = bfs(atlantic)
            
        return list(pacificReachable & atlanticReachable)