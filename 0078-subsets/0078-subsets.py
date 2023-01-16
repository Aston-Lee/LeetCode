class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ## generate all masks
#         n = len(nums)
#         res = []
#         for i in range(2**n, 2**(n+1)):
#             mask = bin(i)[3:]
#             tmp_res = []
#             for j in range(len(nums)):
#                 if mask[j] == '1':
#                     tmp_res.append(nums[j])
#             res.append(tmp_res)

            
#         return res
    
        n = len(nums)
        Res = []
        for i in range(2**n, 2**(n+1)):
            tmpRes = []
            mask = bin(i)[3:]
            for j in range(n):
                if mask[j] == '1':
                    tmpRes.append(nums[j])
            tmpRes = sorted(tmpRes)
            if tmpRes not in Res:
                Res.append(tmpRes[:])

        return Res