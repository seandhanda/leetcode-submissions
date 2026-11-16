class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) -1

        while left <= right:
            mid = (left + right)//2

            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                if nums[mid] > nums[right]:
                    if nums[left] > target:
                        left = mid + 1
                    elif nums[left] <= target:
                        right = mid - 1
                elif nums[mid] <= nums[right]:
                    right = mid - 1

            elif nums[mid] < target:
                if nums[mid] > nums[right]:
                    left = mid + 1
                elif nums[mid] <= nums[right]:
                    if nums[right] >= target:
                        left = mid + 1
                    elif nums[right] < target:
                        right = mid - 1
        return -1
    #O(logn) time
    #O(1) space