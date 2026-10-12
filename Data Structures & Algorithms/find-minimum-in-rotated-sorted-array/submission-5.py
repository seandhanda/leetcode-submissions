class Solution:
    def findMin(self, nums: List[int]) -> int:
        solution = float('inf')
        
        left = 0
        right  = len(nums) - 1
         
        while left <= right:
            mid = (left + right) // 2

            if nums[left] <= nums[right]:
                return min(solution, nums[left])

            if nums[mid] < solution:
                solution = nums[mid]

            if nums[mid] >= nums[left]:
                left = mid + 1
            
            elif nums[mid] < nums[left]:
                right = mid - 1

        return solution

        #O(log(n)) time
        #O(1) space 