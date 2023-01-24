class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashtable = defaultdict(int)
        for i in nums:
            hashtable[i] += 1
            
        for i in hashtable:
            if hashtable[i] == 1:
                return i
        
                
        
        