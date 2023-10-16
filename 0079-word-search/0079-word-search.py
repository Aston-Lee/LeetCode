class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS, COLS = len(board), len(board[0])
        path = set()
        
        NEI = [(0,1), (1,0), (0,-1), (-1,0)]
        def dfs(r, c, i):
            if (r,c) in path:
                return False
            if i == len(word)+1:
                return True
            
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return False
            elif board[r][c] != word[i-1]:
                return False
                
            path.add((r,c))
            for x, y in NEI:
                if dfs(r+x,c+y,i+1):
                    return True
            path.remove((r,c))
            
            return False
                
            
            
        freq = collections.Counter(word)
        if freq[word[0]] > freq[word[-1]]:
            word = word[::-1]
             
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(r,c,1):
                        return True        
        return False
        
        
            
            
            
            
        