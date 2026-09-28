class Solution:
    def search(self, nums: List[int], target: int) -> int:

        #optiml
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left + right) // 2

            if target == nums[mid]:
                return mid

            if target > nums[mid]:
                if nums[mid] >= nums[left]: #mid is in right section
                    left = mid + 1    
                elif nums[mid] < nums[left]: # mid is in left section
                    if target > nums[right]:
                        right = mid -1
                    elif target <= nums[right]:
                        left = mid + 1
            if target < nums[mid]:
                if nums[mid] >= nums[left]: #mid is in right section
                    if target < nums[left]:
                        left = mid + 1
                    elif target >= nums[left]:
                        right = mid - 1
                elif nums[mid] < nums[left]: # mid is in left section
                    right = mid -1
        return -1

        #O(logn) runtime
        #O(1) space




        # left = 0
        # right = len(nums)-1

        # while left <= right:
        #     mid = (left + right)//2

        #     if nums[mid] > target:
        #         if nums[left] > target:
        #             #9,10,1,2,3,4,8(mid).... and target is 3, BROKEN METHOD!!!!!! 
        #             left = mid + 1
        #         else:
        #             right = mid - 1
        #     if nums[mid] < target:
        #         if nums[right] < target:
        #             right = mid -1
        #         else:
        #             left  = mid + 1    
        #     elif nums[mid] == target:
        #         return mid

        # return -1 

        # #O(logn) time
        # # O(1) space