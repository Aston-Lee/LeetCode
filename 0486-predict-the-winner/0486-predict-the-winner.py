class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        '''
        return True representing player1 can win
        
        [1,5,233,7,2]
        
        if 1 - best([5,233,7,2]) -> -234
               return max( 5 - best(233,7,2), 7 - best(5,233,7) )
                      max( 5 - 233,           7 - -228) -> 235
                               return max((233 - best(7,2)), (2 - best(233,7))
                                                  return max((5-best(233,7)), (7-best(5,233)))
        if 2 - best([1,5,233,7]) -> 
               return max( 1 - best(5, 233,7), 7 - best(1,5,233) )
               return max( 1- -228,            7 - 228) -> 229
                               return max((5 - best(233,7)), (7 - best(5, 233))
                                                   return max((1 - best(5,233)), (233 - best(1,5))
                
        [1,5,2]        
        if 1 - best([5,2]) > 0: return True -> 1-5 = -4 < 0 no return 
               max(5,2) -> 5
                
        if 2 - best([1,5]) > 0: return True -> 2-5 = -3 < 0 no return 
               max(1,5) -> 5
        
        return False


        [1,5,2,4,6]
        1 - best([5,2,4,6]) -> 1 - 5 = -4
            5 - best([2,4,6]) -> 5-2 = 3
                2 - best([4,6]) -> -4
                6 - best([2,4]) -> 2
            6 - best([5,2,4]) -> 6-1 = 5
                5 - best([2,4]) -> 1
                4 - best([5,2]) -> -1
                
        
        '''
        
#         if len(nums) <= 2:
#             return True
        
#         def best(array):
#             if len(array) == 2:
#                 return max(array)
#             else:   
#                 return max(array[0] - best(array[1:]), array[-1] - best(array[:-1]))

#         if nums[0] - best(nums[1:]) >= 0:
#             return True
        
#         if nums[-1] - best(nums[:-1]) >= 0:
#             return True
        
#         return False

        n = len(nums)
        if n % 2 == 0 or n == 1:
            return True
        
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = nums[i]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])

        return dp[0][n - 1] >= 0
        