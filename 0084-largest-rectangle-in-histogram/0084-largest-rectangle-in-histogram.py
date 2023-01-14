class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        MaxArea = 0
        for index, height in enumerate(heights):
            if not stack or height >= stack[-1][1]:
                stack.append([index, height])
            else:
                start, tmpheight = index, height ##not sure 
                while stack and stack[-1][1] > height:
                    start, tmpheight = stack.pop()
                    MaxArea = max(MaxArea, (index-start)*tmpheight)
                stack.append([start, height])
        
        n = len(heights)
        for index, height in stack:
            MaxArea = max( MaxArea, (n-index)*height )
        return MaxArea
                