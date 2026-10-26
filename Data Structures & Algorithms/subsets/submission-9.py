class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        solution = []
        
        entry = []

        def dfs(index: int) -> None:
            if index > (len(nums)-1):
                solution.append(entry.copy())
                return

            entry.append(nums[index])
            dfs(index+1)
            entry.pop()
            dfs(index+1)
        
        dfs(0)
        return solution
        #O(2^n) time
        #O(n) space

                