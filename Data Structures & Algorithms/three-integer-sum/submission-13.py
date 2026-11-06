class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution = []

        #O(nlogn) time
        nums.sort()

        index = 0
        while index < len(nums):
            left = index+1
            right = len(nums)-1

            while left < right:
                total = nums[left]+nums[right]
                target = -nums[index]

                if total == target:
                    solution.append([nums[index],nums[left],nums[right]])
                
                elif total < target:
                    left += 1
                    continue
                elif total > target:
                    right -= 1
                    continue
                
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1


            index += 1
            while index < len(nums) and nums[index] == nums[index-1]:
                index += 1

        return solution

        #O(n^2) time
        #O(1) space