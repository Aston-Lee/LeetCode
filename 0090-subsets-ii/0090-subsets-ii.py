class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
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