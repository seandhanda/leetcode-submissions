class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        solution = []
        entry = []

        nums.sort()

        def dfs(startIndex: int) -> None:
            if startIndex > len(nums)-1:
                solution.append(entry.copy())
                return

            entry.append(nums[startIndex])
            dfs(startIndex + 1)
            entry.pop()
            newIndex = startIndex + 1
            while newIndex < len(nums) and nums[newIndex] == nums[startIndex]:
                newIndex +=1
            dfs(newIndex)

        dfs(0)
        return solution

        #O(n * 2^n) time
        #O(n) space