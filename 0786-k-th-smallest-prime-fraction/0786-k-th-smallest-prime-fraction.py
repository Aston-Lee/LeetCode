class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        
#         minheap  K-th Smallest 
        
        
#         0.5 1 2
#         0.33 1 3
#         0.2 1 5 
#         0.66 2 3
#         0.4 2 5
#         0.6 3 5
        
#         0.2 1 5 
#         0.33 1 3
#         0.4 2 5
#         0.5 1 2
#         0.6 3 5
#         0.66 2 3
        
        minheap = []
        
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                heapq.heappush( minheap, (((arr[i]/arr[j]), arr[i], arr[j])) )
        
        ans = None
        while k:
            ans = heapq.heappop(minheap)
            k -= 1
                               
        return [ans[1], ans[2]]
        
        
        
        
        
        