class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        solution = len(position)
        stack = []

        for i in range(len(position)):
            stack.append((position[i], speed[i]))
        
        stack.sort()

        while stack:
            position, speed = stack.pop()
            time = (target - position) / speed
            while stack and ((target - stack[-1][0])/stack[-1][-1]) <= time:
                stack.pop()
                solution -= 1
        return solution

        #O(n) time
        #O(n) space