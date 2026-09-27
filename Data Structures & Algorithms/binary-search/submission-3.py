class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left<=right:
            mid = (left+right) // 2
            # if overflow (not in python): mid = (left + ((right - left) // 2) )
            # this works for size 3, 2 and size 1 last cases
            if nums[mid] > target:
                right = mid-1
            elif nums[mid] < target:
                left = mid+1
            elif nums[mid] == target:
                return mid
        return -1
        #O(logn) runtime
        #O(1) space