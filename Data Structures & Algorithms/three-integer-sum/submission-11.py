class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution = []
        
        nums.sort()
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            target = -nums[i]
            left = i+1
            right = len(nums) -1
            while left < right:
                total = nums[left] + nums[right]
                if total == target:
                    solution.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left +=1
                    right -=1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif total < target:
                    left +=1
                elif total > target:
                    right -= 1
                
            

        return solution
            #O(n^2) time
            #O(1) space
