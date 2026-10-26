class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # solution = False
        seen = set() # tuple (row, col)

        ROWS, COLS = len(board), len(board[0])

        def dfs(index: int, row: int, col: int) -> bool:
            # nonlocal solution
            
            if index == len(word):
                return True
            if (row < 0 or col < 0 or
                row > ROWS-1 or col > COLS-1 or
                (row, col) in seen or
                board[row][col] != word[index]):
                return
            
            seen.add((row, col))

            if (dfs(index+1, row+1, col) or
                dfs(index+1, row-1, col) or
                dfs(index+1, row, col+1) or
                dfs(index+1, row, col-1)):
                return True

            seen.remove((row,col))
            return False

        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(0, row, col):
                    return True
        
        return False 

        #O(nm * 4^n) time where n is number of rows and m is number of cols
        #O(L) space where n is size of board and m is size of word




