class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
#         ## brute force solution
#         maxEnd = 0
#         for start, end in intervals:
#             maxEnd = max(maxEnd, end)
        
#         booked = [False]*maxEnd
#         for start, end in intervals:
#             for i in range(start, end):
#                 if booked[i] == True:
#                     return False
#                 else:
#                     booked[i] = True
#         return True
        
        if len(intervals) <= 1:
            return True
        
        sorted_intervals = sorted(intervals)
        for i in range(1, len(sorted_intervals)):
            if sorted_intervals[i][0] < sorted_intervals[i-1][1]:
                return False
        return True
    
        
            
    
    
        
        
        


        