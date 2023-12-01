class Solution:
    def numWays(self, s: str) -> int:
        
#        "10101"
#         11223
#         p1 = 1 ( 0,1 ) 1-0+1    = 2
#         p2 = 3 ( 2,3 ) 3-1      = 2 
#         end = 4 ( 4 )  4-3      = 1
        
#         "1001"
#          1112
#         p1 = 2 (0,1,2) 2-0+1    = 3
#         p2 = 3 (3)     3-2      = 1
#         end = 3 ( None ) 3-3    = 0
        
#         "0000"
#          0000
            
#         p1 = 3
#         p2 = 3
#         end = 3

#         1111
#         1234
#         111111
#         12 34 56
        
        
#         10101 3 
#         11223
#         3 -> 1 2 3 
        
#          "0000" 0
#           0000
#         0 -> 0 0 0            
        
        MOD = 10**9 + 7
        arr = []
        tmp = 0
        for char in s:
            tmp += int(char)
            arr.append(tmp)
            
        numset = set(arr)
        if max(arr) % 3 !=0:
            return 0
        elif max(arr) == 0:
            tmp = 0
            for i in range(len(s)-2):
                tmp += i+1
            return tmp%MOD

        else:
            n = max(arr)
            n1, n2, n3 = n/3, 2*n/3, n
            c1, c2, c3 = 0, 0, 0
            for num in arr:
                if num == n1:
                    c1 += 1
                elif num == n2:
                    c2 += 1
                # elif num == n3:
                #     c3 += 1
                else:
                    continue
            return (c1*c2)%MOD
        
# "100100010100110"
#  111222233444566
    
# 4*3*2
    
# 2 4 6 

# "10101"
#  11223

                    
        