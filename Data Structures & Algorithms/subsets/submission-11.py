class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        subset = []

        def dfs(index: int) -> None:
            if index == len(nums):
                subsets.append(subset.copy())
                return
            
            subset.append(nums[index])
            dfs(index + 1)
            subset.pop()
            dfs(index + 1)
            

        dfs(0)
        return subsets

        #O(n * 2^n) time
        #O(n) space