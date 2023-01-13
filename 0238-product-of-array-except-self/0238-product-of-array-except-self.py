class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        
        prefix = []
        res = 1
        for i in range(n-1):
            res*=nums[i]
            prefix.append(res)
        prefix.append(1)
        
        postfix = []
        res = 1
        for i in range(n-1, 0, -1):
            res*=nums[i]
            postfix.append(res)
        postfix.append(1)
        postfix = postfix[::-1]
        
        output = []
        for i in range(n):
            if i == 0:
                output.append(1*postfix[i+1])
            elif i == n-1:
                output.append(prefix[i-1]*1)
            else:
                output.append(prefix[i-1]*postfix[i+1])
                
        return output
        