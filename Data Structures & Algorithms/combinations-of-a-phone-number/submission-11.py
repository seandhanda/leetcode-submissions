class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        solution = []
        temp = ""

        map = {
            "2": ["a","b","c"],
            "3":["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w","x", "y","z"]
        }

        def dfs(index: int) -> None:
            nonlocal temp

            if index > len(digits)-1:
                solution.append(temp)
                return
            
            for i in range(len(map[digits[index]])):
                temp += map[digits[index]][i]
                dfs(index+1)
                temp = temp[:-1]

            return
            

        dfs(0)
        return solution

        #O(n * 4^n) time
        #O(n) space