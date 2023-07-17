class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) %2:
            return False
        
        target = sum(nums) // 2
        dp = set()
        dp.add(0)
        
        for i in range(len(nums)):
            newDP = set()
            for d in list(dp):
                if d + nums[i] == target:
                    return True
                
                # if d + nums[i] < target:
                newDP.add(d + nums[i])
                newDP.add(d)
            dp = newDP
                
        return False