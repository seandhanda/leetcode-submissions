class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #brute force n^2 comparisons building solution array
        #optimal = monotonic decreasing stack
        solution = [0] * len(temperatures)
        stack = []

        for index, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][1]:
                poppedIndex, poppedTemperature = stack.pop()
                solution[poppedIndex] = index - poppedIndex
            stack.append((index, temperature))
        return solution

        #O(n) time
        #O(n) space