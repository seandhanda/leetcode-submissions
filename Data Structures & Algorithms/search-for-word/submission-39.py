class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:        
        seen = set() #tuple (row,col)
        
        def dfs(row: int, col: int, index: int) -> bool:
            if index > len(word)-1:
                return True
    
            elif (row < 0 or col < 0 or
                row > len(board)-1 or col > len(board[0])-1 or
                board[row][col] != word[index] or
                (row, col) in seen):
                return False
            
            
            seen.add((row,col))
            found = (
                dfs(row+1, col, index+1) or
                dfs(row, col+1, index+1) or
                dfs(row-1, col, index+1) or
                dfs(row, col-1, index+1))
            seen.remove((row,col))
            return found

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,0):
                    return True
        return False

        #O(mn * 4^L) time
        #O(L) space