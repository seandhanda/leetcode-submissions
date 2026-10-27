class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) < 1:
            return []
        
        solution = []
        word = ""

        map = {
                "2": ["a","b","c"],
                "3": ["d", "e","f"],
                "4": ["g", "h", "i"],
                "5": ["j", "k", "l"],
                "6": ["m", "n", "o"],
                "7": ["p", "q", "r", "s"],
                "8": ["t", "u", "v"],
                "9": ["w", "x", "y", "z"]}


        def dfs(index: int) -> None:
            nonlocal word

            if index > len(digits)-1:
                solution.append(word)
                return 
            for letter in map[digits[index]]:
                word += letter
                dfs(index+1)
                word = word[:-1]
            
        dfs(0)
        return solution

        #O(n*4^n) time # n work each recursive call comes from not the solution.append, this is O(1), rather it comes from the word += letter because this creates a duplicate object and reassigns the word reference to it. 
        #O(n) space