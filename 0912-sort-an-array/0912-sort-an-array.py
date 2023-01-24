class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums)//2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return self.mergeArray(left, right)
    
    def mergeArray(self, arr1, arr2):
        l, r = 0, 0
        tmparr = []
        while l<len(arr1) and r<len(arr2):
            if arr1[l] < arr2[r]:
                tmparr.append(arr1[l])
                l += 1
            else:
                tmparr.append(arr2[r])
                r += 1
        tmparr += arr1[l:] + arr2[r:]
        return tmparr
        
                              