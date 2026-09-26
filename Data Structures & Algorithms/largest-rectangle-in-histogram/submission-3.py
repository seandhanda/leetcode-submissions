class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #Optimal:
        solution = 0

        stack = []
       
        for i,h in enumerate(heights):
            starterTracker = i                      # need i for tracking length difference, needstarterTracker for when appending i,h
            while stack and h < stack[-1][1]:
                startIndex, height = stack.pop()
                if solution < (i - startIndex)*(height):
                    solution  = (i - startIndex)*(height)
                starterTracker = startIndex
            stack.append((starterTracker,h))

        while stack:
            index = len(heights)
            startIndex, height = stack.pop()
            if solution < ((index - startIndex)*height):
                solution = ((index - startIndex)* height)

        return solution

        #O()time
        #O()space


        # # brute force - double iteration
        # solution = 0
        # if len(heights) == 1:
        #     return heights[0]
        # for i in range(len(heights)):
        #     temp = heights[i]
        #     minHeight = heights[i]
        #     for j in range(i+1, len(heights),+1):
        #         minHeight = min(heights[j],minHeight)
        #         if (minHeight * (j-i+1)) > temp:
        #             temp = (minHeight * (j-i+1))
        #     if solution < temp:
        #         solution = temp
        # return solution

        # #O(n^2) runtime
        # #O(1) space

