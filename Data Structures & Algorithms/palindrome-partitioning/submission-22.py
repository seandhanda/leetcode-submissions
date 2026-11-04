class Solution:
    def partition(self, s: str) -> List[List[str]]:
        solution  = []
        temp = []

        def dfs(startIndex: int) -> None:
            if startIndex > len(s)-1:
                solution.append(temp.copy())
                return 
            
            for i in range(startIndex+1, len(s), +1):
                if validPalindrome(startIndex, i):
                    temp.append(s[startIndex: i+1])
                    dfs(i+1)
                    temp.pop()
            temp.append(s[startIndex])
            dfs(startIndex+1)
            temp.pop()

        def validPalindrome(start: int, end: int) -> bool:
            left = start
            right = end

            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True

        dfs(0)
        return solution 

        #O(n * 2^n) time
        #O(n) space