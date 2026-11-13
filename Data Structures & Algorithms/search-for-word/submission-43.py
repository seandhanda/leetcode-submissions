class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # found = False

        seen = set() #tuples of squares

        def dfs(row: int, col: int, index: int) -> bool:
            # nonlocal found
            # if index == len(word):
            #     found = True
            #     return
            if (row > len(board)-1 or col > len(board[0])-1 or
                row < 0 or col < 0 or
                (row, col) in seen or
                board[row][col] != word[index]):
                return False
            if index == len(word)-1:
                return True

            
            seen.add((row, col))
            if (
                dfs(row+1, col, index + 1) or
                dfs(row, col + 1, index + 1) or
                dfs(row-1, col, index+1) or
                dfs(row, col-1, index+1)):
                return True
            seen.remove((row,col))


        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,0):
                    return True
        return False

        #O(mn * 4^L) time
        #O(L) space