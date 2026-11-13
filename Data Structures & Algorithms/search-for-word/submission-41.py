class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        found = False

        seen = set() #tuples of squares

        def dfs(row: int, col: int, index: int) -> None:
            nonlocal found
            # if index == len(word):
            #     found = True
            #     return
            if (row > len(board)-1 or col > len(board[0])-1 or
                row < 0 or col < 0 or
                (row, col) in seen or
                board[row][col] != word[index]):
                return
            if index == len(word)-1:
                found = True
                return

            
            seen.add((row, col))
            dfs(row+1, col, index + 1)
            dfs(row, col + 1, index + 1)
            dfs(row-1, col, index+1)
            dfs(row, col-1, index+1)
            seen.remove((row,col))


        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i,j,0)
                if found:
                    return True
        return found

        #O(mn * 4^L) time
        #O(L) space