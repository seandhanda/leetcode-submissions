class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #monotonic decreasing stack
        stack = [] # position, speed

        # cars = []
        # for i in range(len(position)):
        #     cars.append(position[i], speed[i])
        # cars.sort()
        cars = sorted(zip(position,speed))

        for i in range(len(cars)):
            p, s = cars[i]
            time = (target - p)/s
            while stack and time >= ((target - stack[-1][0])/stack[-1][1]):
                stack.pop()
            stack.append((p,s))
        return len(stack)
        #O(nlogn) time
        #O(n) space


        #generic stack
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
