class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        solution = []
        entry = []

        def dfs(startIndex: int) -> None:
            if startIndex > len(s)-1:
                solution.append(entry.copy())
                return
            
            for endIndex in range(startIndex+1, len(s),+1):
                if isValid(startIndex, endIndex):
                    entry.append(s[startIndex:endIndex+1])
                    dfs(endIndex+1)
                    entry.pop()
            entry.append(s[startIndex])
            dfs(startIndex+1)
            entry.pop()
        
        def isValid(startIndex: int, endIndex: int) -> bool:
            while startIndex < endIndex:
                if s[startIndex] != s[endIndex]:
                    return False
                startIndex += 1
                endIndex -= 1
            return True

        dfs(0)
        return solution

        #O(n^3) time
        #O(n) space