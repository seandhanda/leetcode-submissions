class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Optimal:

        solution = []

        nums.sort()

        for i in range(len(nums)-2):
            if nums[i] == nums[i-1] and i>0:
                continue
            target = -nums[i] 
            left = i+1
            right = len(nums)-1

            while left < right:
            #     if left <= len(nums)-1 and nums[left] == nums[left - 1]:
            #         left +=1
            #         continue
                # ^^ INCORRECT BECAUSE IT COMPARES i and j for first iteration
                # if right>=0 and nums[right] == nums[right+1]:
                #     right -=1
                #     continue
                
                if nums[left] + nums[right] < target:
                    left += 1
                    continue
                elif nums[left] + nums[right] > target:
                    right -= 1
                    continue
                elif nums[left] + nums[right] == target:
                    solution.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left <= len(nums)-1 and nums[left] == nums[left-1]:
                        left +=1
                        continue
        return solution
        # O(n^2)time
        #O(1) space
        # WE DO NOT WANT if not in solution, this can be O(n^3) triples in solution, so O(n^4) runtime due ot searching solution list in worst case.

        
        # #brute force - just iterate
        # solution = []

        # for i in range(len(nums)-2):
        #     for j in range(i+1, len(nums)-1,+1):
        #         for k in range(j+1, len(nums),+1):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 if sorted([nums[i],nums[j],nums[k]]) not in solution:
        #                     solution.append(sorted([nums[i], nums[j], nums[k]]))
        # return solution

        # #O(1) space
        # #O(n^3) time