class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        maxA = 0
        l, r = 0, len(height)-1
        while l<r:
            maxA = max(maxA, (r-l)*min(height[l], height[r]))
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return maxA