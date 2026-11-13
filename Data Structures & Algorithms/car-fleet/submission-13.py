class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #monotonic decreasing stack

        cars = sorted(zip(position, speed))

        stack = []

        for i in range(len(cars)):
            time = ((target - cars[i][0]) / cars[i][1])
            while stack and ((target - stack[-1][0]) / stack[-1][1]) <= time:
                stack.pop()
            stack.append(cars[i])

        return len(stack)

        #O(n) time
        #O(n) space