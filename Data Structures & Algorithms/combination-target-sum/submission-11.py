class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        subset = []
        def dfs(start: int, total: int) -> None:
            nonlocal res, subset
            
            if total == target:
                res.append(subset.copy())
                return 
            if total > target:
                return
            if start >= len(nums):
                return
            
            # for i in range(start, len(nums)):
            #     subset.append(nums[i])
            #     dfs(i)
            #     subset.pop()

            subset.append(nums[start])
            dfs(start, total+nums[start])
            subset.pop()
            dfs(start+1, total)
  
        dfs(0, 0)
        return res

        #O(n*2^n) time
        #O(n) space 