class Solution:
    def isValid(self, s: str) -> bool:
        # brute force: n^2 find pairs, remove, should be immediate pair. n iterations, where replace "" is O(n) itself = n^2. #REMOVING 2 at a time =/= log2(n), it = O(n). Dividing by 2 = O(log2(n))
        # while "()" in s or "[]" in s or "{}" in s:
        #     s = s.replace("()","")
        #     s= s.replace("[]","")
        #     s=s.replace("{}", "")
       
        # if s != "":
        #     return False
        # return True

        
        #LIFO =  stack, tur output into string, and compare with str

        map = {"}":"{",
               ")":"(",          
               "]":"["  
               }
        stack = []

        for c in s:
            if c not in map:
                stack.append(c)
            else:
                if len(stack) == 0  or stack.pop() != map[c]:
                    return False
        
        if len(stack) != 0:
            return False

        return True
        


