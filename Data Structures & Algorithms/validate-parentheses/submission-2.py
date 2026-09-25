class Solution:
    def isValid(self, s: str) -> bool:
        # brute force: n^2 find pairs, remove, should be immediate pair. n iterations, where replace "" is O(n) itself = n^2
        while "()" in s or "[]" in s or "{}" in s:
            s = s.replace("()","")
            s= s.replace("[]","")
            s=s.replace("{}", "")
       
        if s != "":
            return False
        return True

        
        #LIFO =  stack, tur output into string, and compare with str

        stack = []
        compare = ""

        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            else:
                if c != stack.pop():
                    return False

        return True


