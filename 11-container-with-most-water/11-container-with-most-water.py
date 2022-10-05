class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # @2 pointer Space:O(n^2) Time:O(1)
        
        l, r = 0, len(height)-1
        tmp_max, all_max = 0, 0
        while l<=r :
            tmp_max = (r-l)*min(height[l], height[r])
            if all_max < tmp_max :
                all_max = tmp_max
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        
        return all_max
        