class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        oneSet = set()
        twoSet = set()
        
        count = 0
        i = 0
        popped = 0
        while i != len(nums):
            n = nums[i]
            if n not in oneSet:
                oneSet.add(n)
            elif n in oneSet and n not in twoSet:
                twoSet.add(n)
            elif n in twoSet:
                nums.pop(i)
                popped += 1
                continue 
            count += 1
            i += 1  
            
        return count
                
        