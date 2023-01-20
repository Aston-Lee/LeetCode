class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        startarr , endarr = [], []
        
        for start, end in intervals:
            startarr.append(start)
            endarr.append(end)
            
        sortedStart = sorted(startarr, reverse=True)
        sortedEnd = sorted(endarr, reverse=True)
        
        
        maxroom, roomnum = 0, 0
        
        for i in range(sortedEnd[0]+1):
            while sortedStart and i >= sortedStart[-1]:
                roomnum += 1
                sortedStart.pop()
                
            while sortedEnd and i >= sortedEnd[-1]:
                roomnum -= 1
                sortedEnd.pop()
            
            maxroom = max(maxroom, roomnum)
        
        return maxroom