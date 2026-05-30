class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
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

        # 3X3 sub blocks with step size 3
        k=0
        rs,re=0,3  # 3,3+3, 6,6+3  0,3  
        cs,ce=0,3  # 0,3    0,3    3,3+3
        while k<9:
            existing=[]
            for i in range(rs,re):
                for j in range(cs,ce):
                    temp=board[i][j]
                    if temp!="." and temp in existing:
                        return False
                    elif temp!=".":
                        existing.append(temp)
            if re==9:
                rs,re=0,3
                cs=ce
                ce+=3
            else:
                rs=re
                re+=3   
            k+=1
        return True
        
                