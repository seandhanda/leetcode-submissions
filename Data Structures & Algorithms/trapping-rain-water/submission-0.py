class Solution:
    def trap(self, height: List[int]) -> int:
        #Intuition:

        #Approach: 

        #Time:

        #Space: 

        #Code:

        solution = 0
        left = 0 
        right = len(height)-1
        maxLeft = height[0]
        maxRight = height[len(height)-1]

        for i in range(len(height)):
            if maxLeft <= maxRight:
                if maxLeft - height[left] > 0:
                    solution += maxLeft - height[left]
                maxLeft = max(maxLeft,height[left])
                left += 1
            else:
                if maxRight - height[right] > 0:
                    solution += maxRight - height[right]
                maxRight = max(maxRight,height[right])
                right -= 1
        return solution
                


        #brute force: does same thing as Option 1, but instead of building maxLeft and maxRight in smart way (max(maxLeft[i-1], height[i])), you iterate across everything to the left and right instead of immediate neighbour = n work instead of 1 work = O(n^2) runtime, O(n) space

        #Option 1: O(n) runtime, O(n) space
        # n = len(height)

        # maxLeft = [0] * n
        # maxRight = [0] * n

        # # Build maxLeft
        # for i in range(1, n):
        #     maxLeft[i] = max(maxLeft[i - 1], height[i - 1])

        # # Build maxRight
        # for i in range(n - 2, -1, -1):
        #     maxRight[i] = max(maxRight[i + 1], height[i + 1])

        # water = 0

        # for i in range(n):
        #     trapped = min(maxLeft[i], maxRight[i]) - height[i]

        #     if trapped > 0:
        #         water += trapped

        # return water


        #Option 2: O(n) runtime, O(1) space:
