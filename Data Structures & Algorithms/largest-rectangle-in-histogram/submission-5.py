class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #Optimal:
        solution = 0

        stack = []
       
        for i,h in enumerate(heights):
            startIndexTracker = i                      # need i for tracking length difference, needstarterTracker for when appending i,h
            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                if solution < (i - index)*(height):
                    solution  = (i - index)*(height)
                startIndexTracker = index
            stack.append((startIndexTracker, h))

        while stack:
            lastIndex = len(heights)
            index, height = stack.pop()
            if solution < ((lastIndex - index)*height):
                solution = ((lastIndex - index)* height)

        return solution

        #O(n)time - even though inner and outter loop, the inner loop runs n total time throughout algo = n+n = O(n)
        #O(n)space


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













#THIS DOES NOT WORK, because when you add stack.append(h), its stack index =/= its start index

        # for i,h in enumerate(heights):
        #     # starterTracker = i                      # need i for tracking length difference, needstarterTracker for when appending i,h
        #     while stack and h < stack[-1]:
        #         height = stack.pop()
        #         if solution < (i - len(stack)-1)*(height):
        #             solution  = (i - len(stack)-1)*(height)
        #     stack.append(h)

        # while stack:
        #     lastIndex = len(heights)
        #     index = len(stack)-1
        #     height = stack.pop()
        #     if solution < ((lastIndex - index)*height):
        #         solution = ((lastIndex - index)* height)

        # return solution
