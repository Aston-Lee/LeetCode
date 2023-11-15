class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        
        
        # minheap = sorted(arr)
        arr.sort()
        minheap = arr
        arr[0] = 1
        heapq.heapify(minheap)
        
        heapq.heappop(minheap)
        largest = 1
        while minheap:
            if abs(minheap[0]-largest) <= 1:
                if minheap[0] > largest:
                    largest = minheap[0]
            else:
                largest += 1
            heapq.heappop(minheap)
                
        return largest
            
        
        