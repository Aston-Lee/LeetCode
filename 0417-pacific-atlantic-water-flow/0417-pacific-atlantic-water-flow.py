class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        DIR = [(0,1), (0,-1), (1,0), (-1,0)]
        m, n = len(heights), len(heights[0])
        
        pacific_reachable, atlantic_reachable = set(), set()
        # pacific_visited, atlantic_visited = set(), set()
        
        def bfs(dq):
            visitedSet = set()
            reachable = set()
            while dq:
                for _ in range(len(dq)):
                    i, j = dq.popleft()
                    reachable.add((i,j))
                    for (_x, _y) in DIR:
                        ni, nj = i+_x, j+_y
                        if 0<=ni<m and 0<=nj<n:
                            if (ni,nj) not in visitedSet and heights[i][j] <= heights[ni][nj]:
                                dq.append((ni,nj))
                                visitedSet.add((ni,nj))
                    # print(reachable)
            return reachable
        
        ## do pacific
        dq = deque()
        for i in range(m):
            if i == 0:
                for j in range(n):
                    dq.append((0,j))
            else:
                dq.append((i,0)) 
        pacific_reachable = bfs(dq)
        
        
        ## do atlantic
        dq = deque()
        for i in range(m):
            if i == m-1:
                for j in range(n):
                    dq.append((m-1,j))
            else:
                dq.append((i,n-1))
        atlantic_reachable = bfs(dq)
        
        return list(pacific_reachable & atlantic_reachable)