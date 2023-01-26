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
                box = [0]*N
                for k in range(3):
                    for z in range(3):
                        if board[3*i+k][3*j+z] != '.':
                            if (box[int(board[3*i+k][3*j+z])-1]) == 1:
                                return False
                            else:
                                box[int(board[3*i+k][3*j+z])-1] = 1
        # check row
        for i in range(N):
            box = [0]*N
            for j in range(N):
                if board[i][j] != '.':
                    if (box[int(board[i][j])-1]) == 1:
                        return False
                    else:
                        box[int(board[i][j])-1] = 1
        
        #check column
        for j in range(N):
            box = [0]*N
            for i in range(N):
                if board[i][j] != '.':
                    if (box[int(board[i][j])-1]) == 1:
                        return False
                    else:
                        box[int(board[i][j])-1] = 1
        
        return True
        
        # check row
        
        
        
        