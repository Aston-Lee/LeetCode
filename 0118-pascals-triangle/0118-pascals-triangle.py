class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        # n=1 1
        # n=2 1 1
        # n=3 1 2 1
        # n=4 1 3 3 1 
        # n=5 1 4 6 4 1
        
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]

        else:
            ans = [[1],[1,1]]
            n = 3
            while n != numRows+1:
                tmp = [1]
                for i in range(1, n-1):  
                    tmp.append(ans[-1][i-1] + ans[-1][i])
                tmp.append(1)
                n+=1
                ans.append(tmp)

        return ans 