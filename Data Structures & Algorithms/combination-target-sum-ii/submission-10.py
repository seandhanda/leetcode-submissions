class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
      solution = []
      entry = []
      candidates.sort()
      
      def dfs(total: int, index: int) -> None:
        if target == total:
            solution.append(entry.copy())
            return
        if total > target or index > len(candidates)-1:
            return

        entry.append(candidates[index])
        dfs(total + candidates[index], index+1)

        newIndex = index + 1
        while newIndex < len(candidates) and candidates[newIndex] == candidates[index]:
            newIndex += 1        
        entry.pop()
        dfs(total, newIndex)
    
      dfs(0,0)
      return solution

      #O(n*2^n) time
      #O(n) space