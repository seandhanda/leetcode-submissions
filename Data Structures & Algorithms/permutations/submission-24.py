class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        solution = [] 
        temp = []
        lookup = set()

        def dfs(startIndex: int) -> None:
            if len(temp) == len(nums):
                solution.append(temp.copy())
                return
            if startIndex > len(nums)-1:
                return
            if startIndex not in lookup:
                temp.append(nums[startIndex])
                lookup.add(startIndex)
                dfs(0)
                temp.pop()
                lookup.remove(startIndex)
            dfs(startIndex+1)

        dfs(0)
        return solution

        #O(n * n!) time
        #O(n) space