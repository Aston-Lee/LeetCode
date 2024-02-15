class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        
#          [1,12,1,2,5,50,3]
#          [50,12,5,3,2,1,1]
#          [1,1,2,3,5,12,50]
#          prefix sum
#          [0,1,2,4,7,12,24]

            
#         [5,5,5]
#         [0,5,10]
        
        nums.sort()
        prefixsum = [0]
        psum = 0
        for i in range(len(nums)-1):
            psum += nums[i]
            prefixsum.append(psum)
        
        for i in range(len(nums)-1, 1, -1):
            if prefixsum[i] > nums[i]:
                return prefixsum[i] + nums[i]
        return -1
        