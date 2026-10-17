class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        solution = []

        used = set()
        subset = []

        def dfs(start: int) -> None:
            if start >= len(nums):
                return
            if len(subset) == len(nums):
                solution.append(subset.copy())
                return
            
            if start not in used:
                subset.append(nums[start])
                used.add(start)
                dfs(0)
                subset.pop()
                used.remove(start)
            dfs(start + 1)


        dfs(0)
        return solution
