class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
    

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minStack) == 0:
            self.minStack.append(val)
        else: 
            minValue = min(val, self.minStack[-1])
            self.minStack.append(minValue)
        #O(1) time
        #O(1) space

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
    
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
