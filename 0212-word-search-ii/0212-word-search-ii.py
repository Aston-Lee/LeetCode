class TrieNode:
    def __init__(self):
        self.child = {}
        self.isEnd = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        self.root = TrieNode()
        self.ans = set()
        
        ## build a tree out of words
        def _buildTree(w):
            node = self.root
            for char in w:
                if char not in node.child:
                    node.child[char] = TrieNode()
                node = node.child[char]
            node.isEnd = True
    
        for word in words:
            _buildTree(word)
        
        

#         def _check(x, y):
#             visited = set()

#             def dfs(_x, _y, thisnode, string):
#                 if thisnode.isEnd:
#                     self.ans.add(string)

#                 visited.add((_x, _y))  # Mark the current cell as visited

#                 for _i, _j in NEI:
#                     nx, ny = _x + _i, _y + _j
#                     if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
#                         if board[nx][ny] in thisnode.child:
#                             dfs(nx, ny, thisnode.child[board[nx][ny]], string + board[nx][ny])

#                 visited.remove((_x, _y))  # Backtrack: remove the current cell from visited

#             node = self.root
#             if board[x][y] in node.child:
#                 dfs(x, y, node.child[board[x][y]], board[x][y])
        ## search from board
        m, n = len(board), len(board[0])
        NEI = [(0,1), (0,-1), (1,0), (-1,0)]
        def _check(x, y):
            # string = ""
            visited = set((x,y))
            def dfs(_x, _y, thisnode, string):
                if thisnode.isEnd:
                    self.ans.add(string)
                    
                visited.add((_x, _y))
                for _i, _j in NEI:
                    nx, ny = _x+_i, _y+_j
                    if 0<=nx<m and 0<=ny<n:
                        if board[nx][ny] in thisnode.child and (nx, ny) not in visited:
                            dfs(nx, ny, thisnode.child[board[nx][ny]], string + board[nx][ny])
                visited.remove((_x, _y))
                return
            
            node = self.root
            if board[x][y] in node.child:
                dfs(x, y, node.child[board[x][y]], board[x][y])
                
            
        
        for i in range(m):
            for j in range(n):
                _check(i,j)
                    
        return list(self.ans)