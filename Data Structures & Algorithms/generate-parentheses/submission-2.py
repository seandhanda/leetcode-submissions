class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        solution = []

        entry = ""

        def dfs(open: int, close: int) -> None:
            nonlocal entry
            
            if open == n and close == n:
                solution.append(entry)
                return

            if open == close:
                open += 1
                entry += "("
                dfs(open, close)
                entry = entry[:-1]
                open -= 1
            
            elif open > close and open < n:
                open +=1
                entry += "("
                dfs(open, close)

                open -= 1
                entry = entry[:-1]
                close += 1
                entry += ")"
                dfs(open, close)
                close -= 1
                entry = entry[:-1]
            elif open > close and open == n:
                close += 1
                entry += ")"
                dfs(open, close)
                entry = entry[:-1]
                close -= 1


        dfs(0,0)
        return solution

        #O() time
        #O(n^2) space
