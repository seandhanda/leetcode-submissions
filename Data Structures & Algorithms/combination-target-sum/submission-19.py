class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        solution = []
        entry = []

        def dfs(index: int, total: int) -> None:
            if total == target:
                solution.append(entry.copy())
                return
            if total > target or index == len(nums):
                return
            
            entry.append(nums[index])
            dfs(index, total + nums[index])
            entry.pop()
            newIndex = index + 1
            while newIndex < len(nums) and nums[index] == nums[newIndex]:
                newIndex += 1
            dfs(newIndex, total)

        dfs(0,0)
        return solution

        #O(nlogn + (n * 2^n)) time
        #O(n) space