class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Rules
        #Each row cannot contain duplicate and must be 1-9
        # Each column cannot contain duplicate and must be 1-9
        # Each 3x3 grid cannot contian duplicate and must be 1-9

        #FOR EVERY CELL: Brute force checks all rules FOR every row, every column, every 9x9 grid

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                value = board[i][j]

                for row in range(9):
                        if (row != i) and (board[row][j] == value):
                            return False

                for column in range(9):
                    if (column != j) and (board[i][column] == value):
                        return False

                startColumn = (j // 3) *3 
                startRow = (i // 3) * 3
                for row in range(startRow, startRow+3, +1):
                    for column in range(startColumn, startColumn+3, +1):
                        if ((row != i) or (column != j)) and (board[row][column] == value):
                            return False

        return True   

        # O(1) not O(n^(3/2))
        # O(1) space                     