class Solution:
    def partition(self, s: str) -> List[List[str]]:
        solution = []

        substring = [] # list of strings

        def validPalindrome(start: int, end: int) -> bool:
            left = start
            right = end

            while left <= right:
                if s[left] != s[right]:
                    return False
                left +=1 
                right -= 1 
            return True


        def dfs(start: int) -> None:
        #THERE IS NO INVALID SUBSTRING CASE

        #if split creates valid palindromic substring, check if complete, if complete: add to solution AND return
            if start > len(s)-1:
                solution.append(substring.copy())
                return


            # substring.append() -YOU CAN DO THIS HERE ADDING CURRENT, or before every dfs as next
            # valid + non finished, continue DFS lookups - SPLIT DECISIONS
            # for i in range(start+1, len(s)-2):
            #     for j in range(j+1, len(s)-1):
            # THIS WILL DOUBLE COUNT VALID SUBSTRINGS THAT START AT SAME PLACE
            for end in range(start, len(s)):
                if validPalindrome(start, end):
                    substring.append(s[start:end+1])
                    dfs(end+1)
                    substring.pop()


        dfs(0)
        return solution

        #O(n*2^n) time
        #O(n + (n * 1) = O(n) space
