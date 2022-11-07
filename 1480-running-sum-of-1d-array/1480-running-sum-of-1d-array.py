class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        tmp = 0
        res = []
        for n in nums:
            tmp += n
            res.append(tmp)
            
        return res