class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = defaultdict(set) # row : set
        COLS = defaultdict(set) # col : set
        GRID = defaultdict(set) # (row//3, col//3) : set


        for row in range(len(board)):
            for col in range(len(board[0])):
                value = board[row][col]
                if value == ".":
                    continue
                elif (
                    value in ROWS[row] or
                    value in COLS[col] or
                    value in GRID[(row//3, col//3)]
                ):
                    return False
                else:
                    ROWS[row].add(value)
                    COLS[col].add(value)
                    GRID[(row//3, col//3)].add(value)
        return True
        
        #fixed size input
        #O(1) time
        #O(1) space
        #variable sized input - n represents rowsxcols:
        #O(n) time
        #O(n) space
        #variable sized input - n rperesents rows or n represents cols
        #O(n^2) time
        #O(n^2) space

                    

