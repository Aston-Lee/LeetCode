class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        
        
#         3 9 1 1 5 8
        
#         1 1 3 5 8 9
        
        pts = [ p[0] for p in points ]
        pts.sort()
        
        widest = 0
        for i in range(len(pts)-1):
            widest = max(widest, pts[i+1] - pts[i])
            
        return widest 
        
        