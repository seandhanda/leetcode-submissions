class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))

        stack = []

        for index, car in enumerate(cars):
            time = ((target - car[0]) / car[1])
            while stack and stack[-1] <= time:
                stack.pop()
            stack.append(time)
        
        return len(stack)

        #O(nlogn) time
        #O(n) space
        

        