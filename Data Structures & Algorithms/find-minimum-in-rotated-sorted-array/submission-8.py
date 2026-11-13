class Solution:
    def findMin(self, nums: List[int]) -> int:
        solution = float('inf')
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right)//2

            if nums[mid] < solution:
                solution = nums[mid]
            
            if nums[right] >= nums[mid]:
                right = mid -1 
                
                
            elif nums[right] < nums[mid]:
                left = mid + 1

        return solution


        #O(logn) time
        #O(1) space