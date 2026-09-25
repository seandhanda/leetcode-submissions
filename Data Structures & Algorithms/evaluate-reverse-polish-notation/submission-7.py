class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)):
        #THis is wrong because negative numbers dont pass this
        #     if tokens[i].isalnum():
            if tokens[i] not in ["+","-","*","/"]:
                stack.append(int(tokens[i]))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                if tokens[i] == "+":
                    solution = op1 + op2
                elif tokens[i] == "-":
                    solution = op1 - op2
                elif tokens[i] ==  "*":
                    solution = op1*op2
                else:
                    solution = int(op1/op2)
                stack.append(solution)

        return stack[-1]    #stack[0] also works!, stack should be 1 element by end no matter what given valid input is requirement
        #O(n) time
        #O(n) space
        # 2 Special Cases:
        # List with one element, return stack[-1] fixes this
        # add to stack via int(token[i]), and you wont have to worry about int(str) anymore!
         



                