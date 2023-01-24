class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        nums.sort()
        
        [1,1,1]
        
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r : 
                if nums[i] + nums[l] + nums[r] == 0:
                    output.append([nums[i], nums[l], nums[r]])
                    l+=1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l+=1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r-=1
                    while r>0 and nums[r] == nums[r+1]:
                        r-=1
        return output