class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        solution = [] 
        temp = []

        def dfs(startIndex: int) -> None:
            if len(temp) == len(nums):
                solution.append(temp.copy())
                return
            if startIndex > len(nums)-1:
                return
            if nums[startIndex] not in temp:
                temp.append(nums[startIndex])
                dfs(0)
                temp.pop()
            dfs(startIndex+1)

        dfs(0)
        return solution

        #O(n * n!) time
        #O(n) space