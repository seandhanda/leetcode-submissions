class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        solution = []
        entry = ""

        def dfs(open: int, close: int):
            nonlocal entry
            if open == close == n:
                solution.append(entry)
                return
            
            if open < n and open > close:
                entry += "("
                dfs(open+1, close)
                entry = entry[:-1]

                entry += ")"
                dfs(open, close+1)
                entry = entry[:-1]

            if open < n and open == close:
                entry += "("
                dfs(open+1, close)
                entry = entry[:-1]

            if open == n and open > close:
                entry += ")"
                dfs(open, close+1)
                entry = entry[:-1]

        dfs(0,0)
        return solution

        #O(n* 4^n) time
        #O(n^2) space