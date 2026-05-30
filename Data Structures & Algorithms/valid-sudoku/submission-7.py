class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows={i:[] for i in range(len(board))}
        cols={i:[] for i in range(len(board))}
        square={(i,j):[] for i in range(3) for j in range(3)}
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in square[(r//3,c//3)]:
                    return False
                rows[r].append(board[r][c])
                cols[c].append(board[r][c])
                square[(r//3,c//3)].append(board[r][c])
        return True