class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
             
        if (sx, sy) == (fx, fy):
            if t > 1 or t == 0:
                return True
            else:
                return False
        
        dx = abs(fx - sx)
        dy = abs(fy - sy)
           
        time = 0
        if dx and dy:
            mindelta = min(dx, dy)
            time += mindelta
            dx -= mindelta
            dy -= mindelta
        
        return time + dx + dy <= t
            