class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = []
        for n in nums:
            if n in seen:
                seen.pop(indexOf(seen,n))
            else:
                seen.append(n)
        return seen[0]
                
        
        