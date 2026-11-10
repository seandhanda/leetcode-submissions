class Solution:
    def isValid(self, s: str) -> bool:
        map = {")":"(",
               "}":"{", 
                "]":"["
                }

        stack = []

        for c in s:
            if c not in map:
                stack.append(c)
            else:
                if len(stack) == 0 or stack.pop() != map[c]:
                    return False
        
        if len(stack) != 0:
            return False
        
        return True

        #O(n) time
        #O(n) space
                
        


