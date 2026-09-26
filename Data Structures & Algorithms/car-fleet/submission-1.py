class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = len(position)

        stack = []
        for i in range(len(position)):
            stack.append((position[i],speed[i]))
        stack.sort()

        while stack:
            position, speed = stack.pop()
            time = (target - position) / speed
            while stack and time >= ((target - stack[-1][0])/stack[-1][1]):
                fleet -= 1
                stack.pop()

        return fleet

        # nlogn time
        # n space