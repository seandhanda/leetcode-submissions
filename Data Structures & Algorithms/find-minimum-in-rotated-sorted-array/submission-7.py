class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        minimum = float('inf')


        while left <= right:
            mid = (left + right)//2 
            if nums[mid] < minimum:
                minimum = nums[mid]

            if nums[right] > nums[mid]:
                right = mid - 1
            elif nums[right] <= nums[mid]:
                left = mid + 1
        return minimum
        #O(logn) time
        #O(1) space            
