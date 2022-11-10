class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i, j = len(matrix)-1, 0
        
        while( i>-1 and j<len(matrix[0]) ):
            print(i, j, matrix[i][j])
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                i -= 1
            elif matrix[i][j] < target:
                j += 1
        
        return False
            