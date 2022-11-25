class Solution:
    def findMin(self, nums: List[int]) -> int:
        
#         [4,5,6,7,0,1,2]
        
#         l=4 r=2 mid=7
        
        l, r = 0, len(nums)-1
        allmin = float('inf')
        while l <= r:
            mid = (l + r) // 2
            allmin = min(allmin, nums[mid])
            if nums[l] > nums[r] and nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
            
        return allmin