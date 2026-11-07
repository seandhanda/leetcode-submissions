class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:
            rowMid = (top+bottom)//2
            if target < matrix[rowMid][0]:
                bottom = rowMid-1
            elif target > matrix[rowMid][-1]:
                top = rowMid + 1
            else:
                left = 0
                right = len(matrix[rowMid])-1

                while left <= right:
                    colMid = (left + right)//2
                    total = matrix[rowMid][colMid]
                    if total == target:
                        return True
                    elif total < target:
                        left = colMid + 1
                    elif total > target:
                        right = colMid - 1
                return False
        return False

        #O(logn) time
        #O(1) space


