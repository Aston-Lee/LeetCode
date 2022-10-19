class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def dfs(i, l, r):
            while(l<=r):
                mid = (l+r) // 2
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return False
        
        for i in range(len(matrix)):
            if matrix[i][0] == target or target == matrix[i][-1]:
                return True
            elif matrix[i][0] < target and target < matrix[i][-1]:
                return dfs(i, 0, len(matrix[i]))
            
                