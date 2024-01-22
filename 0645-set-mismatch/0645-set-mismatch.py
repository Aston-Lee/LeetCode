class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        mySet = set(nums)
        
        ans = [None, None]
        
        freq = collections.Counter(nums)
        
        for key, val in freq.items():
            if val == 2:
                ans[0] = key
                break
        
        for i in range(1,n+1):
            if i not in mySet:
                ans[1] = i
                break
                
        return ans
    
    
    
                