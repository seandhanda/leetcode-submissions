class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Optimal
        solution = 0

        left = 0
        right = len(heights)-1

        while left < right:
            temp = (right - left) * min(heights[right], heights[left])
            if temp > solution:
                solution = temp
            if heights[left] <= heights[right]:
                left += 1
            elif heights[right] < heights[left]:
                right -= 1
        return solution
        #O(1)space
        #O(n) time


 
 
 
        # #brute force iterate across every line

        # solution = 0

        # for i in range(len(heights)-1):
        #     for j in range(i+1,len(heights),+1):
        #         temp = (j-i) * min(heights[i], heights[j])
        #         if temp > solution:
        #             solution = temp
        #             continue
        # return solution
        # #TIme O(n^2)
        # #Space O(1)