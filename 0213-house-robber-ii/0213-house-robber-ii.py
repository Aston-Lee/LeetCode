class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        num1 = nums[:-1]
        num2 = nums[1:]
        
        def dpfunction(arr) -> int: ##return the last of dp, which is the larget of the result
            dp = [0]*(len(arr)+1) ##1-based 
            ## note that the arr we passed in is a 0-based 
            for i in range(len(arr)+1):
                if i < 3:
                    dp[i] = arr[i-1]
                elif i == 3:
                    dp[i] = max(dp[1]+arr[2], dp[2])
                else: # i>=4
                    dp[i] = max(dp[i-2], dp[i-3]) + arr[i-1]
                print(dp)
            print("end if dp", dp)
            return max(dp[-1],dp[-2])
            
        return max(dpfunction(num1), dpfunction(num2))
            
            
            