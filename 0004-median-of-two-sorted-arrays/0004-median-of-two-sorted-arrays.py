class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
#         min max heap?

        
#         nums1 = [ -n for n in nums1]
#         heapq.heapify(nums1)
#         print(nums1)

#         [1, 3, 5, 7]  -> 4 5 6 7
#         [2, 4, 6]  -> -3 -2 -1
        
        ## balances the array 
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        
        heapq.heapify(nums1) ## min heap
        
        nums2 = [-n for n in nums2]
        heapq.heapify(nums2) ## maxheap
        
        
        while(len(nums1) - len(nums2) >= 2):
            num = heapq.heappop(nums1)
            heapq.heappush(nums2, -num)
            
        if nums2 == []:
            return nums1[0]
            
        ## while(maxheap max is bigger than minheap min, swap both element)
        while(nums1[0] < -nums2[0]):
            small = heapq.heappop(nums1)
            big = heapq.heappop(nums2)
            
            heapq.heappush(nums1, -big)
            heapq.heappush(nums2, -small)
            
        # print(nums1, nums2)
        if len(nums1) > len(nums2):
            return nums1[0]
        else:
            return (nums1[0] + -nums2[0])/2
            
 