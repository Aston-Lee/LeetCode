class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        
        CountIndex = {0:-1}
        maxlength = 0
        count = 0
        for i, num in enumerate(nums):
            if num == 0:
                count -= 1
            else:
                count += 1 
            # print(count, i)
            if count not in CountIndex:
                CountIndex[count] = i
            else:
                maxlength = max(maxlength, i-CountIndex[count])
            # print(CountIndex)
            # print('-----')
                
        return maxlength
        