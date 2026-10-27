class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) < 1:
            return []
        
        solution = []
        word = ""

        def dfs(index: int) -> None:
            nonlocal word

            if index > len(digits)-1:
                solution.append(word)
                return 

            if digits[index] == "2":
                word +=  "a" 
                dfs(index + 1)
                word = word[:-1]   
                word += "b"
                dfs(index + 1)
                word = word[:-1]   
                word += "c"
                dfs(index+1)
                word = word[:-1]    
            elif digits[index] == "3":
                word +=  "d" 
                dfs(index + 1)
                word = word[:-1] 
                word += "e"
                dfs(index + 1)
                word = word[:-1] 
                word += "f"
                dfs(index+1)
                word = word[:-1]  
            elif digits[index] == "4":
                word +=  "g" 
                dfs(index + 1)
                word = word[:-1]    
                word += "h"
                dfs(index + 1)
                word = word[:-1]   
                word += "i"
                dfs(index+1)
                word = word[:-1]   
            elif digits[index] == "5":
                word +=  "j" 
                dfs(index + 1)
                word = word[:-1]  
                word += "k"
                dfs(index + 1)
                word = word[:-1]  
                word += "l"
                dfs(index+1)
                word = word[:-1]    
            elif digits[index] == "6":
                word +=  "m" 
                dfs(index + 1)
                word = word[:-1]    
                word += "n"
                dfs(index + 1)
                word = word[:-1]   
                word += "o"
                dfs(index+1)
                word = word[:-1]    
            elif digits[index] == "7":
                word +=  "p" 
                dfs(index + 1)
                word = word[:-1]   
                word += "q"
                dfs(index + 1)
                word = word[:-1]   
                word += "r"
                dfs(index+1)
                word = word[:-1]  
                word += "s"
                dfs(index+1)
                word = word[:-1]  
            elif digits[index] == "8":
                word +=  "t" 
                dfs(index + 1)
                word = word[:-1]   
                word += "u"
                dfs(index + 1)
                word = word[:-1]    
                word += "v"
                dfs(index+1)
                word = word[:-1]    
            elif digits[index] == "9":
                word +=  "w" 
                dfs(index + 1)
                word = word[:-1]    
                word += "x"
                dfs(index + 1)
                word = word[:-1]    
                word += "y"
                dfs(index+1)
                word = word[:-1]    
                word += "z"
                dfs(index+1)
                word = word[:-1]    

        dfs(0)
        return solution

        #O(n*4^n) time
        #O(n) space