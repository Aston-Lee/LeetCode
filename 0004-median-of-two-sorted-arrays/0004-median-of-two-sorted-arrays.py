class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Find the median of two sorted arrays.

        The function implements a binary search algorithm to find the median in a time complexity of O(log(min(m, n))).

        Args:
        nums1 (List[int]): First sorted array.
        nums2 (List[int]): Second sorted array.

        Returns:
        float: The median of the two arrays.

        Time Complexity: O(log(min(m, n))) - binary search is performed on the smaller of the two arrays.
        Space Complexity: O(1) - constant space used.
        """
        # Ensure nums1 is the smaller array to minimize the binary search time
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        imin, imax = 0, m
        half_len = (m + n + 1) // 2

        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i

            # Binary search adjustment
            if i < m and nums2[j-1] > nums1[i]:
                # i is too small, increase it
                imin = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                # i is too big, decrease it
                imax = i - 1
            else:
                # i is perfect
                if i == 0: max_of_left = nums2[j-1]
                elif j == 0: max_of_left = nums1[i-1]
                else: max_of_left = max(nums1[i-1], nums2[j-1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m: min_of_right = nums2[j]
                elif j == n: min_of_right = nums1[i]
                else: min_of_right = min(nums1[i], nums2[j])

                return (max_of_left + min_of_right) / 2.0
