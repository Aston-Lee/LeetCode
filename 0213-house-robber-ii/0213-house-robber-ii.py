class Solution:
    def rob(self, nums: List[int]) -> int:
        
#         [200,3,140,20,10]
        
#         [200,3,340,220] 340
#         [3,140,23,150] 150
        
        
        if len(nums) == 1:
            return nums[0]
        
        ls1 = nums[:-1]
        ls2 = nums[1:]
        
        def robber(ls):
            n = len(ls)
            if n<2:
                return max(ls)
            if n == 3:
                ls[2] += ls[0]
                return max(ls)
            dp = [0]*n
            for i in range(n):
                if i<2:
                    dp[i] = ls[i]
                elif i==2:
                    dp[2] = dp[i-2] + ls[i]
                else:
                    dp[i] = max(dp[i-2], dp[i-3]) + ls[i]
            print(dp)
            return max(dp)
                    
        return max(robber(ls1), robber(ls2))
                
            