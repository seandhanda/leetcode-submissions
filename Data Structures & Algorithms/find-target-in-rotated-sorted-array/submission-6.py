class Solution:
    def search(self, nums: List[int], target: int) -> int:
        solution = -1
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2 

            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                if nums[mid] >= nums[left]:
                    if nums[left] > target:
                        left = mid + 1
                    elif nums[left] <= target:
                        right = mid - 1
                elif nums[mid] < nums[left]:
                    right = mid - 1 
            elif nums[mid] < target:
                if nums[mid] >= nums[left]:
                    left = mid + 1
                elif nums[mid] < nums[left]:
                    if target > nums[right]:
                        right = mid - 1
                    elif target <= nums[right]:
                        left = mid + 1
                
        return solution

        #O(logn) time
        #O(1) space