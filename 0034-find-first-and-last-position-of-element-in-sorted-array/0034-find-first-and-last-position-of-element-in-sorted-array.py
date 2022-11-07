class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        l, r = 0, len(nums)-1
        tl, tr = -1, -1
        while(l <= r):
            mid = (l+r) // 2
            if nums[mid] == target:
                tl = tr = mid
                break
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        if tl != -1 and tr != -1:
            while(True):
                if tl-1 > -1 and nums[tl-1] == target:
                    tl -= 1
                else:
                    break
                    
            while(True):
                if tr+1 < len(nums) and nums[tr+1] == target:
                    tr += 1
                else:
                    break
            
        return [tl, tr]
                