class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ### use mask
        ### crucial to think of bitmap, and how to successfully generate th bitmap
        subsets = []
        for i in range(2**len(nums), 2**(len(nums)+1)):
            bitmap = bin(i)[3:]
            print(bitmap)
            subset = []
            for j in range(len(bitmap)):
                if bitmap[j] == '1':
                    subset.append(nums[j])
            subsets.append(subset)
        
        return subsets
