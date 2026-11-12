class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        
        solution = []
        entry = []

        def dfs(index: int, total: int) -> None:
            if total == target:
                solution.append(entry.copy())
                return
            if total > target or index == len(candidates):
                return
            
            entry.append(candidates[index])
            dfs(index+1, total + candidates[index])
            entry.pop()
            newIndex = index + 1
            while newIndex < len(candidates) and candidates[newIndex] == candidates[index]:
                newIndex += 1
            dfs(newIndex, total)

        dfs(0,0)
        return solution

        #O(n * 2^n) time
        #O(n) space
