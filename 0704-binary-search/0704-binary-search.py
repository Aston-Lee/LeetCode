class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def bs(l,r):
            mid = (l + r)// 2
            print(nums[mid])
            if nums[mid] == target:
                return mid
            if l >= r:
                return -1
            if nums[mid] > target:
                return bs(l, mid-1)
            else:
                return bs(mid+1, r)
        
        return bs(0,len(nums)-1)
                
            
                
            