class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = len(position)

        # stack = []
        # for i in range(len(position)):
        #     stack.append((position[i],speed[i]))
        #Replace ALL of the above with:
        stack = [[p,s] for p,s in zip(position, speed)]
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

#         # intuition (why is this stack pattern when starting problem):
#         very briefly what is the intuition behind "oh this is stack problem"
# Because after sorting cars by position, each car only needs to compare against the fleet immediately ahead of it.

# A stack naturally tracks those unresolved fleets:

# New car catches top fleet → merge/pop
# Doesn't catch it → becomes a new fleet/push
# Key recognition: "Compare current item to the most recent relevant item, possibly remove it" → stack.