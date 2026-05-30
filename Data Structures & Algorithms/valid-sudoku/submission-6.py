class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        submatrix={}
        # Row wise validation
        for i in range(9):
            rexisting=[]
            cexisting=[]
            for j in range(9):
                row=board[i][j]
                col=board[j][i]
                if row !="." and row in rexisting:
                    return False
                if col != "." and col in cexisting:
                    return False
                if row!=".":
                    rexisting.append(row)
                if col!=".":
                    cexisting.append(col)
                
                loc=f"{i//3},{j//3}"
                if loc not in submatrix:
                    submatrix[loc]=[]
                if board[i][j]!="." and board[i][j] in submatrix[loc]:
                    return False
                submatrix[loc].append(board[i][j])
        return True
        
                