class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        
#         ## O(nlogn) / O(n)
        sortintervals = sorted(intervals, key = lambda x: x[0])
        res = []
        for interval in sortintervals:
            if len(res) == 0:
                res.append((interval[0], interval[1]))
                continue
            if interval[0] <= res[-1][1]:
                if interval[1] > res[-1][1]:
                    res[-1] = (res[-1][0], interval[1])
                else: 
                    continue
            else:
                res.append(interval)
                
        return res  