class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        # Initialize a set to keep track of the painted intervals
        seen = {}
        work_log = []
        
        for start, end in paint:
            work = 0            
            while start < end:
                if start in seen: 
                    tmp = seen[start]
                    seen[start] = max(seen[start], end) # more compress
                    start = tmp                                                            
                else:
                    seen[start] = end
                    work += 1
                    start += 1  
            work_log.append(work)
                    
        return work_log
