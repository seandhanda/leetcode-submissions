class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        solution = []
        entry = []

        nums.sort()

        def dfs(index: int) -> None:
            if index == len(nums):
                solution.append(entry.copy())
                return
            
            entry.append(nums[index])
            dfs(index+1)
            entry.pop()
            newIndex = index + 1
            while newIndex < len(nums) and nums[index] == nums[newIndex]:
                newIndex+=1
            dfs(newIndex)

        dfs(0)
        return solution

        #O(n * 2^n) time
        #O(n) space