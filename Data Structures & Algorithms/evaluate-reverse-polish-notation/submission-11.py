class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # problem guarangees valid input, so len(tokens) == 1, 
        if len(tokens) == 0:
            return 0
        # if len(tokens) == 1
        #     return tokens[0]

        stack = []

        for i in range(len(tokens)):
            if tokens[i] not in ["+", "-", "*", "/"]:
                stack.append(int(tokens[i]))
            else:
                opRight = stack.pop()
                opLeft = stack.pop()
                if tokens[i] == "+":
                    res = opLeft + opRight
                elif tokens[i] == "-":
                    res = opLeft - opRight
                elif tokens[i] == "*":
                    res = opLeft * opRight
                elif tokens[i] == "/":
                    res = int(opLeft / opRight)
                stack.append(res)

        return stack[-1]
 
        #O(n) time
        #O(n) space


                