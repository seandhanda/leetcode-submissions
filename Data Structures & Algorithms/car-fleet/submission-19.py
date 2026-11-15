class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        fleet = len(position)

        stack = []
        for car in cars:
            stack.append(car)
        
        while stack:
            indexPosition, indexSpeed = stack.pop()
            time = ((target - indexPosition) / indexSpeed)
            while stack and time >= ((target - stack[-1][0]) / stack[-1][1]):
                stack.pop()
                fleet -= 1
        return fleet

        