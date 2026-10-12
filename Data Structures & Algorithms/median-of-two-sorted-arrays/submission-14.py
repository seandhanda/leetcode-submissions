class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        totalSize = len(nums1) + len(nums2)
        half = (totalSize // 2) 

        if len(nums1) <= len(nums2):
            A= nums1
            B = nums2
        else:
            A = nums2
            B = nums1

        left = 0 
        right = len(A) - 1
        
        while True:
        
            mid = (left + right) // 2

            jIndex = ((half) - (mid+1))-1
        
            bLeft = B[jIndex] if jIndex >= 0 else float('-inf')
            bRight = B[jIndex + 1] if (jIndex + 1) < len(B) else float('inf')
            aLeft = A[mid] if mid >= 0 else float('-inf')
            aRight = A[mid + 1] if (mid+1) < len(A) else float('inf')

            #checks:
            if bLeft <= aRight and aLeft <= bRight:
                if totalSize % 2:
                    return min(aRight, bRight)
                else:
                    return (max(aLeft, bLeft) + min(aRight, bRight)) / 2

            else:
                if bLeft > aRight:
                    left = mid + 1
                elif aLeft > bRight:
                    right = mid - 1

        #O(log(n)) where n is min(len(nums1), len(nums2))
        #O(1) space