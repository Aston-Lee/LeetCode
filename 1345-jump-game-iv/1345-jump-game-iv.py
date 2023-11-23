class Solution:
    def minJumps(self, arr: List[int]) -> int:
        
#         [100,-23,-23,404,100,23,23,23,3,404]
        
#         100 : 0 4
#         -23 : 1 2
#         404 : 3 9
#         23  : 5 6 7
#         3   : 8
        
        
#         start 100
#         end 404 (9)   
        
        
#         bfs
        
#         visited: set(0,4,1,3,5,2,9) ## whenever got put into dq, add to visited 
#         dq = [3,5,2,9]
#         time = 2    
        
#         1. check same num
#         2. check i+1
#         3. check i-1

        visited = set([0])
        dq = deque([0])
        time = 0
        end = len(arr)-1
        
        adj = defaultdict(list)
        for i, num in enumerate(arr):
            adj[num].append(i)
            
        while dq:
            time += 1
            for _ in range(len(dq)):
                idx = dq.popleft()
                if idx == end:
                    return time-1
                # _add(idx)
                for ids in adj[arr[idx]]:
                    if ids not in visited:
                        dq.append(ids)
                        visited.add(ids)
                adj[arr[idx]].clear() ## note this line 
                if idx-1 >=0 and idx-1 not in visited:
                    dq.append(idx-1)
                    visited.add(idx-1)
                if idx+1 < len(arr) and idx+1 not in visited:
                    dq.append(idx+1)
                    visited.add(idx+1)
             
        
    