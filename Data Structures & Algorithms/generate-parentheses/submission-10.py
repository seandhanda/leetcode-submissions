class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        solution = []
        entry = ""

        def dfs(open: int, close:int) -> None:
            nonlocal entry
            
            if open == close == n:
                solution.append(entry)
                return 

            elif open == close:
                entry += "("
                dfs(open+1, close)
                entry = entry[:-1]

            elif open > close and open < n:
                entry += ")"
                dfs(open, close + 1)
                entry = entry[:-1]    
                
                entry += "("
                dfs(open+1, close)
                entry = entry[:-1]
            
            elif open > close and open == n:
                entry += ")"
                dfs(open, close+1)
                entry = entry[:-1]

                
        dfs(0,0)
        return solution

        #O(2^n) time
        #O(n) space