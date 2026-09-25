class MinStack:

    def __init__(self):
        self.stack = []
        self.MinStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.MinStack:
            self.MinStack.append(val)
        # elif self.MinStack[-1] <= val:
        #     self.MinStack.append(self.MinStack[-1])
        # elif self.MinStack[-1] > val:
        #     self.MinStack.append(val)
        #You can replace all of the above with this:
        else:
            minVal = min(val,self.MinStack[-1])
            self.MinStack.append(minVal)

    def pop(self) -> None:
        self.stack.pop()
        self.MinStack.pop()
    
    def top(self) -> int:
        # return self.stack[len(self.stack)-1]
        return self.stack[-1]

    def getMin(self) -> int:
        return self.MinStack[-1]
        
