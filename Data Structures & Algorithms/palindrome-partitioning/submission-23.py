class Solution:
    def partition(self, s: str) -> List[List[str]]:
        solution = []
        entry = []

        def dfs(startIndex : int) -> None:
            if startIndex == len(s):
                solution.append(entry.copy())
                return
            
            for endIndex in range(startIndex+1, len(s),+1):
                if isValidPalindrome(startIndex, endIndex):
                    entry.append(s[startIndex:endIndex+1])
                    dfs(endIndex+1)
                    entry.pop()
            entry.append(s[startIndex])
            dfs(startIndex+1)
            entry.pop()
            
        def isValidPalindrome(leftIndex: int, rightIndex: int) -> bool:
            while leftIndex < rightIndex:
                if s[leftIndex] != s[rightIndex]:
                    return False
                leftIndex += 1
                rightIndex -= 1
            return True

        dfs(0)
        return solution

        #O(n * 2^n) time
        #O(n) space


