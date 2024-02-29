class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        
        DIR = [(2,1),(1,2),(-2,-1),(-1,-2),(-2,1),(-1,2),(2,-1),(1,-2)]
        dq = deque([(0,0)])
        time = 0
        visited = set((0,0))
        while dq:
            time += 1
            for _ in range(len(dq)):
                i, j = dq.popleft()
                if (i,j) == (x,y):
                    return time-1
                for _x, _y in DIR:
                    ni, nj = i+_x, j+_y
                    if (ni, nj) not in visited:
                        dq.append((ni, nj))
                        visited.add((ni, nj))
                        
            
            