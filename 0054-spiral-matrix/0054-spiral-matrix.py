class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        direction  = {
            (0,1) : (1,0),
            (1,0) : (0,-1),
            (0,-1) : (-1,0),
            (-1,0) : (0,1)
        } 
        seen = set() #store the pos
        
        m = len(matrix)
        n = len(matrix[0])
        
        q = deque()
        q.append((0, 0))
        di, dj = 0,1
        output = []
        endcondition = m*n
        
        while q:
            if len(output) == endcondition:
                break
            i, j = q.popleft()
            seen.add((i,j))
            output.append(matrix[i][j])
            if 0<=i+di<m and 0<=j+dj<n and (i+di, j+dj) not in seen:
                q.append((i+di,j+dj))
            else:
                di, dj = direction[(di, dj)]
                q.append((i+di,j+dj))
                # print(di, dj)
        
        return output