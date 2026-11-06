class Solution:
    def maxArea(self, heights: List[int]) -> int:
        solution = 0
        left = 0
        right = len(heights)-1

        while left < right:
            total = min(heights[left], heights[right]) * abs(right-left)
            if total > solution:
                solution = total
            if heights[left] >= heights[right]:
                right -= 1
            elif heights[left] < heights[right]:
                left += 1
        
        return solution

        #O(n) time
        #O(1) space