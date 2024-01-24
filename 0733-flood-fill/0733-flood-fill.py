class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        ## bfs
        DIR = ((0,1), (0,-1), (1,0), (-1,0))
        m, n = len(image), len(image[0])
        
        dq = deque([[sr, sc]])
        visited = set((sr, sc))
        self.original_color = image[sr][sc]
        while dq:
            i, j = dq.popleft()
            image[i][j] = color
            for x, y in DIR:
                ni, nj = i+x, j+y
                if 0 <= ni < m and 0 <= nj < n:
                    if image[ni][nj] == self.original_color and (ni, nj) not in visited:
                        visited.add((ni, nj))
                        dq.append([ni, nj])
                    
        return image
        
        
        
            