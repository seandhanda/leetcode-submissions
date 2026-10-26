class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        solution = []
        entry = []

        def dfs(total: int, index: int) -> None:
             if total == target:
                solution.append(entry.copy())
                return
             if total > target or index > (len(nums)-1):
                return
            
             entry.append(nums[index])
             dfs(total+nums[index], index)
             entry.pop()
             dfs(total, index+1)

        dfs(0, 0)
        return solution

        #O(n*) time
        #O(target/min index value) space