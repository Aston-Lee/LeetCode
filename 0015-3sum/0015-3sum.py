class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        [-1,0,1,2,-1,-4].sort()
        [-4,-1,-1,0,1,2]
                  p l r
             
        [[-1,-1,2], [-1,0,1]]

        '''
        nums.sort()
        res = []
        p = 0
        while p < len(nums)-2:
            l = p+1
            r = len(nums)-1
            while l<r:
                if nums[p] + nums[l] + nums[r] == 0:
                    res.append([nums[p], nums[l], nums[r]])
                    while l<r and l<len(nums)-1 and nums[l] == nums[l+1]:
                        l += 1
                    while l<r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif nums[p] + nums[l] + nums[r] < 0:
                    l+=1
                else:
                    r-=1
            while p<len(nums)-2 and nums[p] == nums[p+1]:
                    p += 1
            p+=1
            
                    
        return res
            
            
            
        