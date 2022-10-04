class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ## prefix postfix no optimize
#         prefix = []
#         pre = 1
#         for n in nums:
#             pre *= n
#             prefix.append(pre)
            
#         postfix = []
#         post = 1
#         for n in nums[::-1]:
#             post *= n
#             postfix.append(post)
#         postfix = postfix[::-1]
        
#         output = [0]*len(prefix)
#         for i in range(len(prefix)):
#             if i == 0:
#                 output[i] = 1*postfix[i+1]
#             elif i == len(prefix)-1:
#                 output[i] = prefix[i-1] * 1
#             else:
#                 output[i] = prefix[i-1] * postfix[i+1]
#         return output
        
        ## prefix postfix optimize
        output = []
        res = 1
        for i in range(len(nums)):
            if i == 0:
                output.append(1)
            else:
                res *= nums[i-1]
                output.append(res)

        res = 1
        for j in range(len(nums)-1, -1, -1):  ## start, end_bound(lower), howmany
            
            if j == len(nums)-1:
                output[j] *= 1
            else:
                res *= nums[j+1]
                output[j] *= res
                
        return output
                
            