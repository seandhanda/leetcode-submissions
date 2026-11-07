class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums)-1

        while left <= right:
            mid = (left+right)//2

            if nums[mid] == target:
                return mid
            
            elif nums[mid] > target:
                if nums[right] >= nums[mid]:
                   right = mid - 1
                elif nums[right] < nums[mid]:
                    if nums[right] >= target:
                        left = mid + 1
                    elif nums[right] < target:
                        right = mid - 1
            elif nums[mid] < target:
                if nums[right] >= nums[mid]:
                    if nums[right] >= target:
                        left = mid + 1
                    elif nums[right] < target:
                        right = mid - 1
                elif nums[right] < nums[mid]:
                    left = mid + 1
        return -1 

        #O(logn) time
        #O(1) space