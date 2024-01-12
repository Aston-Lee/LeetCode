# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        '''
        bm is a object
        mat[i] is sorted in non-decreasing order.
        
        if use binary search in each mat[i]? (log(100) -> 2)
        200 api calls at max
        binary search is not possible 
        
        '''
        bm = binaryMatrix
        # print(bm.get(0,0), bm.get(0,1), bm.get(1,0), bm.get(1,1))
        m, n = bm.dimensions()
        # print(m,n)
        
        def bs(i):
            l, r = 0, n-1
            found = False 
            while l <= r:
                mid = (l+r)//2
                if bm.get(i, mid):
                    found = True
                    r = mid - 1
                else:
                    l = mid + 1
            
            return l if found else m
        
        minPos = float('inf')
        for i in range(m):
            minPos = min(minPos, bs(i))
            
        return minPos if minPos != m else -1
        
            