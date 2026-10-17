class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #set is best for lookup
        path = set()

        ROWS, COLS = len(board), len(board[0])

        solution = False

        def dfs(row: int, col: int, index: int) -> None:
            nonlocal solution
            
            if (col < 0  or row < 0 or 
                col >= COLS or row >= ROWS or # because COLS and ROWS are size, not last index
                (row, col) in path or
                word[index] != board[row][col]):
                    return

            if index == len(word)-1:
                solution = True
                return
            
            path.add((row, col))
            dfs(row, col+1, index + 1)
            dfs(row + 1, col, index + 1)
            dfs(row - 1, col, index + 1)
            dfs( row, col-1, index + 1)
            path.remove((row, col))

        for i in range(ROWS):
            for j in range(COLS):
                dfs(i,j,0)
                if solution:
                    return solution
        return solution

        #O(nm * nm) time WRONG!!!!!!!!!!!
        #No. Your mistake is assuming DFS visits each cell at most once across the entire search of one iteration starting point. It doesn't
        #O(nm * 3L) time
        #O(L) space











# #OPTION 1
# def dfs(r, c, i):
#     if i == len(word):
#         return True

#     # Check bounds, character, visited...

#     visited.add((r, c))

#     found = (
#         dfs(r + 1, c, i + 1) or
#         dfs(r - 1, c, i + 1) or
#         dfs(r, c + 1, i + 1) or
#         dfs(r, c - 1, i + 1)
#     )

#     visited.remove((r, c))
#     return found




# #OPTION 2
# found = False

# def dfs(r, c, i):
#     nonlocal found

#     if i == len(word):
#         found = True
#         return


        