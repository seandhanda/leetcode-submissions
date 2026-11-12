class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        solution = []
        entry = []

        seen = set()


        def dfs(index: int) -> None:
            # if len(seen) == len(nums)
            if len(entry) == len(nums):
                solution.append(entry.copy())
                return
            if index == len(nums):
                return
            
            if index not in seen:
                entry.append(nums[index])
                seen.add(index)
                dfs(0)
                entry.pop()
                seen.remove(index)
            dfs(index+1)


        dfs(0)
        return solution

        #O(n * n!) time
        #O(n) space