class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # # Optimal O(log(mn)) time
        # top = 0
        # bottom = len(matrix)-1

        # while top <= bottom:
        #     row = (bottom+top)//2
        #     if target > matrix[row][-1]:
        #         top = row+1
        #     elif target < matrix[row][0]:    
        #         bottom = row-1
        #     else:
        #         left = 0
        #         right = len(matrix[row])-1
        #         while left <= right:
        #             mid = (left+right) // 2
        #             if target < matrix[row][mid]:
        #                 right = mid-1
        #             elif target > matrix[row][mid]:
        #                 left = mid + 1
        #             elif target == matrix[row][mid]:
        #                 return True
        #         return False        #what happens if target is not found in a row, without return False, we go back to outer loop and redo creating infinite loop
        # return False
        #O(logm + logn) = log(mn) time
        #O(1) space

        # One loop inside another DOES NOT AUTOMATICALLY mean multiple for runtime. It can be addition!


        
        
        # #brute force, iterative search (not even binary search)
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[i])):
        #         if matrix[i][j] == target:
        #             return True
        # return False
        # #O(mn)time
        # #O(1) space


        #optimized brute force binary search m times
        for i in range(len(matrix)):
            left = 0
            right = len(matrix[i])-1

            while left <= right:
                mid = (left + right) // 2

                if target < matrix[i][mid]:
                    right = mid -1
                elif target > matrix[i][mid]:
                    left = mid + 1
                elif target == matrix[i][mid]:
                    return True

        return False 
        #O(mlogn) runtime
        #O(1) space