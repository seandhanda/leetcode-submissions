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
                #needed because its called later
            elif open > close and open == n:
                close += 1
                entry += ")"
                dfs(open, close)
                #WE NEED TO KEEP the entry point because:
                # entry is declared nonlocal. Every recursive call shares the same variable, so changes persist after returning.
                # we dont need close because:
                # close is a local parameter of each dfs() call. Reassigning it doesn't affect the caller's close, so no restoration is needed if it's not used again.
                entry = entry[:-1]
                close -= 1

            


        dfs(0,0)
        return solution

        #O(n*2^(2n)) = O(n*4^n) time
        #O(n^2) space
