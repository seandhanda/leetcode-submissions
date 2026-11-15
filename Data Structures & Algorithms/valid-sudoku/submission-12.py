class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = defaultdict(set) # 9 keys : set()
        COLS = defaultdict(set) # 9 keys : set()
        GRID = defaultdict(set) # (9 tuples from 0,0 to 3,3) : set()

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == ".":
                    continue
                if (board[row][col] in ROWS[row] or
                    board[row][col] in COLS[col] or
                    board[row][col] in GRID[(row//3, col//3)]):
                    return False
                else:
                    ROWS[row].add(board[row][col])
                    COLS[col].add(board[row][col])
                    GRID[(row//3,col//3)].add(board[row][col])
        return True

        #O(n*n) time
        #O(n*n) space
                    
