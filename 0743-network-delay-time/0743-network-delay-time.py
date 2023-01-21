class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        # using minheap, djistra aldorithm
        
        adjlist = defaultdict(list) #(time to go to the next node, nextnode)
        for u, v, w in times:
            adjlist[u].append((w,v))
            
        seen = set()
        
        minheap = [] # (pathsum, currnode) 
        heapq.heappush(minheap,(0,k))
        
        while(minheap):
                       
            currpathtime, currnode = heapq.heappop(minheap)
            if currnode in seen:
                continue
            seen.add(currnode)
            
            t = currpathtime
            
            for pathtime, newnode in adjlist[currnode]:
                if newnode not in seen:
                    heapq.heappush(minheap, (currpathtime + pathtime , newnode))

        return t if len(seen) == n else -1
        
        
        