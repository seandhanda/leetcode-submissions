class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        solution = []

        nums.sort()

        subset = []

        def dfs(start: int) -> None:
            if start >= len(nums):
                solution.append(subset.copy())
                return
            
            subset.append(nums[start])
            dfs(start+1)
            subset.pop()
            
            nextIndex = start + 1
            while nextIndex < len(nums) and nums[nextIndex] == nums[start]:
                nextIndex += 1
            
            dfs(nextIndex)

        dfs(0)
        return solution

        #O(n * 2^n) time
        #O(n) space