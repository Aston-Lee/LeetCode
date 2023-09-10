class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        @functools.lru_cache(maxsize = None)
        def remain(n):
            if n == 0:
                return 1
            ans = 0
            for num in nums:
                if n-num >= 0:
                    ans += remain(n-num)
                else:
                    break
            return ans
            
        return remain(target)
                
            