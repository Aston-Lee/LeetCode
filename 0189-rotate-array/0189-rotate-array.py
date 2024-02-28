class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
#         1 2 3 4 5 6 7
        
#         7 6 5 4 3 2 1
        
#         5 6 7 1 2 3 4
        
        # @ brute 
        # num = nums[::-1]
        # num = num[:k][::-1] + num[k:][::-1]
        # for i in range(len(nums)):
        #     nums[i] = num[i]
        
        
        n = len(nums)
        k = k%n
        for i in range(n//2):
            nums[i], nums[n-1-i] = nums[n-1-i], nums[i]
        
        for i in range(k//2):
            print(i, k-1-i)
            nums[i], nums[k-1-i] = nums[k-1-i], nums[i]
            
        for i in range((n-k)//2):
            nums[k+i], nums[n-1-i] = nums[n-1-i], nums[k+i]

        
            
        