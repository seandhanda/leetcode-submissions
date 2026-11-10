class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
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
