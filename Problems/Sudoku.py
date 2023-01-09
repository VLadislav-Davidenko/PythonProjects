import collections
class Solution:
    def isValidSudoku(self, board):
        row_set = collections.defaultdict(set)
        column_set = collections.defaultdict(set)
        square = collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in row_set[r] or board[r][c] in column_set[c] or board[r][c] in square[(r//3, c//3)]:
                    return False
                row_set[r].add(board[r][c])
                column_set[c].add(board[r][c])
                square[(r // 3,c // 3)].add(board[r][c])
        return True

S = Solution()
print(S.isValidSudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))