class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        freq = Counter(nums)
        ans = 0 
        for key, val in freq.items():
            ans += val * (val-1) // 2
        
        return ans