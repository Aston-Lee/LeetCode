class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []
        t = 0
        while t != len(nums):
            
            l, r = t+1, len(nums)-1
            while l < r:
                if nums[t] + nums[l] + nums[r] == 0:
                    res.append([nums[t],nums[l],nums[r]])
                    while l < r and l+1 != len(nums) and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and r-1 != 0 and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif nums[t] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1
            
            while t != len(nums)-1 and nums[t] == nums[t+1]:
                t += 1
            t += 1
            
        return res