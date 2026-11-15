class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []

        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(token)
                continue
            opRight = int(stack.pop())
            opLeft = int(stack.pop())
            if token == "+":
                res = opLeft + opRight
            elif token == "-":
                res = opLeft - opRight
            elif token == "*":
                res = opLeft * opRight
            elif token == "/":
                res = int(opLeft / opRight)
            stack.append(res)
        return stack[-1]

        #O(n) time
        #O(n) space

