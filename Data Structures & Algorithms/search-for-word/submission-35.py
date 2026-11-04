class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        solution = False
        if len(word) == 0:
            return True
        
        seen = set() #tuple (row,col)
        
        def dfs(row: int, col: int, index: int) -> None:
            nonlocal solution
            if index > len(word)-1:
                solution = True
                return
            elif (row < 0 or col < 0 or
                row > len(board)-1 or col > len(board[0])-1 or
                board[row][col] != word[index] or
                (row, col) in seen):
                return
            
            
            seen.add((row,col))
            dfs(row+1, col, index+1)
            dfs(row, col+1, index+1)
            dfs(row-1, col, index+1)
            dfs(row, col-1, index+1)
            seen.remove((row,col))

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i,j,0)
                if solution:
                    return True
        return False

        #O(mn * 4^L) time
        #O(L) space