class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        def dfs(x, y, value):
            rooms[x][y] = value
            for (offset_x, offset_y) in [(1,0), (-1,0), (0,1), (0,-1)]:
                if 0 <= x+offset_x < m and 0 <= y+offset_y < n and \
                rooms[x+offset_x][y+offset_y] != -1 and \
                (rooms[x+offset_x][y+offset_y]==float('INF') or value+1 < rooms[x+offset_x][y+offset_y]):
                    dfs(x+offset_x, y+offset_y, value+1)
            return

        m, n = len(rooms), len(rooms[0])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    dfs(i, j, 0)
        
        return rooms