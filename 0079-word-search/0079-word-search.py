class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        DIR = [(0,1), (0,-1), (1,0), (-1,0)]
        self.ans = False
        visited = set()
        def dfs(i, j, wordIndex):
            if wordIndex == len(word)-1:
                self.ans = True
                return
            for _x, _y in DIR:
                ni, nj = i+_x, j+_y
                if 0<=ni<m and 0<=nj<n:
                    if word[wordIndex+1] == board[ni][nj] and (ni, nj) not in visited :
                        visited.add((i,j))
                        dfs(ni,nj,wordIndex+1)
                        visited.remove((i,j))
            return         
            
        m, n = len(board), len(board[0])
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited.add((i,j))
                    dfs(i, j, 0)
                    visited = set()
                    
        return self.ans