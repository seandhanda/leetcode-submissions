class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #brute force, iterative search (not even binary search)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == target:
                    return True
        return False
        #O(mn)time
        #O(1) space