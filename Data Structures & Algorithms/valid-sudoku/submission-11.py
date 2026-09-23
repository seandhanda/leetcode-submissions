class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
       # Optimal - we arent building the columns, rows, and square first and then performing check.
       #Also, we aren't building one set for rows, one for columns, rather, we are building 9 row and 9 columns
       # Lastly, combining the two, we iterate across the board, updating all 3 hashmaps of 9 sets each, and performing valid check SAME time (not at the end) = O(n^2 because set lookup and dict lookup is constant and there are n^2 cells) time, O(n^2) space. Brute Force would have been O(1) space O(n^3)
        columns = defaultdict(set) # only 9 columns
        rows = defaultdict(set)    # only 9 rows
        square = defaultdict(set) # only 9

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                
                value = board[i][j]
            
                # tuplerow = i//3
                # tuplecolumn= j//3
                # squareKeyLookup = (tuplerow, tuplecolumn)

                if value in columns[j] or value in rows[i] or value in square[(i//3,j//3)]: #or value in square[squareKeyLookup]:
                    return False
                columns[j].add(value)
                rows[i].add(value)
                square[(i//3,j//3)].add(value)
        
        return True
       
       
        #Rules
        #Each row cannot contain duplicate and must be 1-9
        # Each column cannot contain duplicate and must be 1-9
        # Each 3x3 grid cannot contian duplicate and must be 1-9

        #FOR EVERY CELL: Brute force checks all rules FOR every row, every column, every 9x9 grid

        # for i in range(9):
        #     for j in range(9):
        #         if board[i][j] == ".":
        #             continue

        #         value = board[i][j]

        #         for row in range(9):
        #                 if (row != i) and (board[row][j] == value):
        #                     return False

        #         for column in range(9):
        #             if (column != j) and (board[i][column] == value):
        #                 return False

        #         startColumn = (j // 3) *3 
        #         startRow = (i // 3) * 3
        #         for row in range(startRow, startRow+3, +1):
        #             for column in range(startColumn, startColumn+3, +1):
        #                 if ((row != i) or (column != j)) and (board[row][column] == value):
        #                     return False

        # return True   

        # O(1) not O(n^(3/2))
        # O(1) space                     