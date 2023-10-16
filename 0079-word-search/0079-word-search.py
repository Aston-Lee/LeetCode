class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ## use copy.deepcopy for deepcopy
        ## in order to fit the time complexity, check the less freq char in words and invert if you need to 
        ## if boardDict[word[0]] > boardDict[word[-1]]:
        ##    word = word[::-1]
        
        neighbor = ((0,1), (1,0), (0,-1), (-1,0))
        
        m = len(board)
        n = len(board[0])
        
        def dfs(i, j, remain, board):
            # print(i, j, remain, board)
            if remain == "":
                return True
            for path in neighbor:
                if (0 <= i + path[0] and i + path[0] < m) \
                    and (0 <= j + path[1] and j + path[1] < n) \
                    and board[i + path[0]][j + path[1]] == remain[0]:
                        tmp = board
                        board[i][j] = -1
                        if dfs(i + path[0], j + path[1], remain[1:], copy.deepcopy(board) ) :
                            return True
                        board = tmp
            return False
        
        boardDict = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in boardDict:
                    boardDict[board[i][j]] += 1
                else:
                    boardDict[board[i][j]] = 1
        
        wordDict = Counter(word)
        for k in wordDict:
            if k not in boardDict or wordDict[k] > boardDict[k]:
                return False
            
        ## this is so crucial
        if boardDict[word[0]] > boardDict[word[-1]]:
            word = word[::-1]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, word[1:], copy.deepcopy(board)) == True:
                        return True
        
        return False