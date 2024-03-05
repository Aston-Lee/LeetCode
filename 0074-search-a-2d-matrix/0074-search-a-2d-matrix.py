class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # decide col
        
        m, n = len(matrix), len(matrix[0])
        
        max_element = matrix[-1][-1] + 1
        matrix.append([max_element] * n)
        # print(matrix)
        
        
        l, r = 0, m-1
        index = None
        while l <= r:
            mid = (l+r)//2
            # print(l, r, mid)
            if matrix[mid][0] <= target < matrix[mid+1][0]:
                index = mid 
                break
                
            if matrix[mid][0] <= target and matrix[mid+1][0] <= target:
                l = mid + 1
            else:
                r = mid - 1
        
        # print(index)
        if index == None:
            return False 
                
        l, r = 0, n-1
        while l <= r:  
            mid = (l+r) // 2
            if matrix[index][mid] == target:
                return True
            
            if matrix[index][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
            
            
        return False 
        