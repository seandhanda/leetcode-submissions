class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        solution = [0] * len(temperatures)

        stack = []

        for index, temperature in enumerate(temperatures):
            while stack and stack[-1][1] < temperature:
                stackIndex, stackTemperature = stack.pop()
                solution[stackIndex] = index - stackIndex
            stack.append((index, temperature))

        return solution
        
        #O(n) time
        #O(n) space
