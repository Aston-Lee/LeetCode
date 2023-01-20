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
        
        
        sorted_intervals = sorted(intervals)
        currMaxEnd = 0
        for start, end in sorted_intervals:
            if start < currMaxEnd:
                return False
            currMaxEnd = max(currMaxEnd, end)
        return True
    
    
            
    
    
        
        
        


        