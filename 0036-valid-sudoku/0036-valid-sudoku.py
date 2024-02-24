import numpy

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        m, n = len(board), len(board[0])
        
        ## check col
        for i in range(m):
            appeared = set()
            for j in range(n):
                if  board[i][j] == '.':
                    continue
                elif board[i][j] in appeared:
                    return False
                else:
                    appeared.add(board[i][j])
                    

        ## check rol
        board = numpy.transpose(board)
        for i in range(m):
            appeared = set()
            for j in range(n):
                if  board[i][j] == '.':
                    continue
                elif board[i][j] in appeared:
                    return False
                else:
                    appeared.add(board[i][j])
        board = numpy.transpose(board)

        
        ## check block
        def _checkblock(i ,j):
            appeared = set()
            for _x in range(3):
                for _y in range(3):
                    if  board[i+_x][j+_y] == '.':
                        continue
                    elif board[i+_x][j+_y] in appeared:
                        return False
                    else:
                        appeared.add(board[i+_x][j+_y])
            return True
        
        for i in range(m/3):
            for j in range(n/3):
                if not _checkblock(3*i, 3*j):
                    return False
        
        return True
        