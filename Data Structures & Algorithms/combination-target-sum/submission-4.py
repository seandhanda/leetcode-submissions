class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        subset = []
        def dfs(start: int) -> None:
            nonlocal res, subset
            
            subsetSum = 0
            for i in range(len(subset)):
                subsetSum += subset[i]
            if subsetSum == target:
                res.append(subset.copy())
                return 
            if subsetSum > target:
                return
            
            for i in range(start, len(nums)):
                subset.append(nums[i])
                dfs(i)
                subset.pop()
        dfs(0)
        return res

        #O(n*2^n) time
        #O(n) space 