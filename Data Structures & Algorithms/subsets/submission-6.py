class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #iterative approach (no backtracking)
        res = [[]]

        for i in range(len(nums)):
            for j in range(len(res)):
                res.append(res[j] + [nums[i]])
        
        return res

        #O(n* 2^n) time
        #O(1) space

        
        
        
        
        # #2 Approaches:
        # #Fastest: nested loop
        # #Backtrack via DFS Decision Tree
        # res = []

        # subset = []
        # def dfs(i: int) -> None:
        #     if i >= len(nums):
        #         res.append(subset.copy())
        #         return
            
        #     subset.append(nums[i])
        #     dfs(i+1)

        #     subset.pop()
        #     dfs(i+1)

        # dfs(0)
        # return res

        # #O(n * 2^n) runtime
        # #O(n) space