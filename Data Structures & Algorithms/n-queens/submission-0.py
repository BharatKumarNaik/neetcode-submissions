class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col_set=set()
        posDig_set=set() # (r+c) will be same for all positive diagonal positions. upward
        negDig_set=set() # (r-c) will be same for all negative diagonal positions. downward
        res=[]
        board=[["."]*n for i in range(n)]
        def backtracking(r):
            if r==n:
                copy=["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in col_set or (r+c) in posDig_set or (r-c) in negDig_set:
                    # we can't place the queen here
                    continue
                col_set.add(c)
                posDig_set.add(r+c)
                negDig_set.add(r-c)
                board[r][c]="Q"

                backtracking(r+1)

                col_set.remove(c)
                posDig_set.remove(r+c)
                negDig_set.remove(r-c)
                board[r][c]="."
        backtracking(0)
        return res