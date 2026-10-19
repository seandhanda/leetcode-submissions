class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # insead of returning [""], we want to return []
        if not digits:
            return []
        
        solution = []

        represent = ""

        map = {
                "2":["a", "b", "c"],
                "3":["d", "e", "f"],
                "4":["g", "h", "i"],
                "5":["j", "k", "l"],
                "6":["m", "n", "o"],
                "7":["p", "q", "r", "s"],
                "8":["t", "u", "v"],
                "9":["w", "x", "y", "z"]}

        def dfs(index: int) -> None:
            nonlocal represent
            
            if index == len(digits):
                solution.append(represent)
                return
            
            for value in map[digits[index]]:
                 represent += value
                 dfs(index+1)
                 represent = represent[0:-1]

        dfs(0)
        return solution
     
        #O(n * 4^n) time
        #O(n) space