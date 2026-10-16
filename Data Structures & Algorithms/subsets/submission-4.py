class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #2 Approaches:
        #Fastest: nested loop
        #Backtrack via DFS Decision Tree
        res = []

        subset = []
        def dfs(i: int) -> None:
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
            dfs(i+1)

        dfs(0)
        return res

        #O(n * 2^n) runtime
        #O(n) space