import numpy as np

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        def check(idx):
            appeared = set()
            for num in board[idx]:
                if num == '.':
                    continue
                if num in appeared:
                    return False
                appeared.add(num)
            return True
                
            
        def checkblock(i, j):
            appeared = set()
            for _x in range(3):
                for _y in range(3):
                    if board[i+_x][j+_y] == '.':
                        continue
                    if board[i+_x][j+_y] in appeared:
                        return False
                    appeared.add(board[i+_x][j+_y])
            return True
        
            
        for i in range(9):
            if not check(i):
                return False
        
            
        for i in range(0,9,3):
            for j in range(0,9,3):
                if not checkblock(i,j):
                    return False
           
        
        board = np.transpose(board)
        for i in range(9):
            if not check(i):
                return False   
            
        return True
        
            
            
            
        
        
        
        
        