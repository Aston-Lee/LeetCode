class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
#         [2,0,2,1,1,0]
        
#         2 0 2 1 1 0
#         0 2 2 1 1 0
#         0 2 1 2 1 0
#         0 2 1 1 2 0
#         0 2 1 1 0 2
        
        
#         ## @bubble sort
#         for i in range(1, len(nums)):
#             for j in range(0, len(nums)-1):
#                 if nums[j] > nums[i] :
#                     nums[i], nums[j] = nums[j], nums[i]
#         return nums
        
        ## @quick sort
        def quicksort(arr, low, high):
            if low < high:
                # Partition the array
                pi = partition(arr, low, high)

                # Recursively apply the same logic to the left and right sub-arrays
                quicksort(arr, low, pi-1)  # Before pi
                quicksort(arr, pi+1, high)  # After pi

        def partition(arr, low, high):
            pivot = arr[high]  # Choose the rightmost element as pivot
            i = low - 1  # Pointer for the greater element
            for j in range(low, high):
                if arr[j] < pivot:
                    i = i + 1
                    arr[i], arr[j] = arr[j], arr[i]

            # Swap the pivot element with the greater element specified by i
            arr[i+1], arr[high] = arr[high], arr[i+1]

            # Return the position from where partition is done
            return i+1

        # Example usage
        arr = [10, 7, 8, 9, 1, 5]
        n = len(nums)
        quicksort(nums, 0, n-1)
        return nums
        
        
        