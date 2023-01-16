class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ## generate all masks
        n = len(nums)
        res = []
        for i in range(2**n, 2**(n+1)):
            mask = bin(i)[3:]
            tmp_res = []
            for j in range(len(nums)):
                if mask[j] == '1':
                    tmp_res.append(nums[j])
            res.append(tmp_res)

            
        return res