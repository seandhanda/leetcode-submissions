class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {
            ")" : "(",
            "}" : "{",
            "]" : "[",
        }

        for c in s:
            if c in map.values():
                stack.append(c)
            elif c in map.keys():
                if not stack or stack.pop() != map[c]:
                    return False
        if stack:
            return False

        return True

        #O(n) time
        #O(n) spcae