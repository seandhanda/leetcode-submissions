class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        solution = []
        temp = []

        def dfs(total: int, index: int):
            if total == target:
                solution.append(temp.copy())
                return
            if index > len(nums)-1:
                return
            if total > target:
                return
            
            temp.append(nums[index])
            dfs(total+nums[index], index)
            temp.pop()
            dfs(total, index+1)

        dfs(0,0)
        return solution

        #O(m * 2^(m+n)) time
        #O(m + n) space