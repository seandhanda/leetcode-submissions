class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        
        solution = False

        current = []

        def dfs(row: int, col: int, index: int) -> None:
            nonlocal solution
            
            if len(current) == len(word):
                solution = True
                return

            elif (row == ROWS or col == COLS or 
                row < 0 or col < 0 or
                (row,col) in current or
                board[row][col] != word[index]):
                    return
          
            
            
            current.append((row, col))
            dfs(row+1,col,index+1) 
            dfs(row, col+1, index+1) 
            dfs(row-1, col, index+1) 
            dfs(row, col-1, index+1)
            current.pop()
                            



        for i in range(ROWS):
            for j in range(COLS):
                dfs(i,j,0)
                if solution:
                    return True
        return False