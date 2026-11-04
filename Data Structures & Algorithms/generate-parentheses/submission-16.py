class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        solution = []
        temp = ""

        def dfs(open: int, close: int) -> None:
            nonlocal temp

            if open == close == n:
                solution.append(temp)
                return
            elif open == n:
                temp += ")"
                dfs(open, close+1)
                temp = temp[:-1]

            elif open < n and open == close:
                temp += "("
                dfs(open+1, close)
                temp = temp[:-1]

            elif open < n:
                temp += "("
                dfs(open+1, close)
                temp = temp[:-1]
                temp += ")"
                dfs(open, close+1)
                temp = temp[:-1]
            
        dfs(0,0)
        return solution

        #O(n * 4^n) time
        #O(n) space