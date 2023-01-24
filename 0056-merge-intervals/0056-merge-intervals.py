class Solution:
    # def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        
#         ## O(nlogn) / O(n)
#         sortintervals = sorted(intervals, key = lambda x: x[0])
#         res = []
#         for interval in sortintervals:
#             if len(res) == 0:
#                 res.append((interval[0], interval[1]))
#                 continue
#             if interval[0] <= res[-1][1]:
#                 if interval[1] > res[-1][1]:
#                     res[-1] = (res[-1][0], interval[1])
#                 else: 
#                     continue
#             else:
#                 res.append(interval)
                
#         return res

#         def mergesort(interval):
#             if len(interval) <= 1:
#                 return interval
#             mid = len(interval) // 2
#             left = mergesort(interval[:m])
#             right = mergesort(interval[m:])
#             return mergetogether(left, right)
        
#         def mergetogether(arr1, arr2):

            
#             return  

    def merge(self, intervals):
        n = len(intervals)
        # merge sort the intervals
        intervals = self.merge_sort(intervals)
        result = []
        for interval in intervals:
            if not result or result[-1][1] < interval[0]:
                # interval does not overlap with previous interval
                result.append(interval)
            else:
                # interval overlaps with previous interval
                # merge intervals by updating the end of the previous interval
                result[-1][1] = max(result[-1][1], interval[1])
        return result

    def merge_sort(self, intervals):
        n = len(intervals)
        if n <= 1:
            return intervals
        mid = n // 2
        left = self.merge_sort(intervals[:mid])
        right = self.merge_sort(intervals[mid:])
        return self.merge_lists(left, right)

    def merge_lists(self, left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i][0] <= right[j][0]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
