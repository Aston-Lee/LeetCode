class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
                
        if len(intervals) == 1:
            return 0
        
        res = 0
        
        sorted_intervals = sorted(intervals)
        prevEnd = sorted_intervals[0][1]
        
        for i in range(1, len(sorted_intervals)):
            if sorted_intervals[i][0] < prevEnd and sorted_intervals[i][1] > prevEnd:
                res += 1
                continue
            elif sorted_intervals[i][0] < prevEnd and sorted_intervals[i][1] <= prevEnd:
                res += 1
            prevEnd = sorted_intervals[i][1]
        
        return res