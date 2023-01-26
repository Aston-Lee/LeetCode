class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        N = len(board)
        # check box
        for i in range(N/3):
            for j in range(N/3):
                seen = set()
                for k in range(3):
                    for z in range(3):
                        if board[3*i+k][3*j+z] != '.': 
                            if board[3*i+k][3*j+z] in seen:
                                return False
                            else:
                                seen.add(board[3*i+k][3*j+z])
                      
        # check row
        for i in range(N):
            seen = set()
            for j in range(N):
                if board[i][j] != '.':
                    if board[i][j] in seen:
                        return False
                    else:
                        seen.add(board[i][j])
        
        #check column
        for j in range(N):
            seen = set()
            for i in range(N):
                if board[i][j] != '.':
                    if board[i][j] in seen:
                        return False
                    else:
                        seen.add(board[i][j])
        
        return True
        
        # check row
        
        
        
        