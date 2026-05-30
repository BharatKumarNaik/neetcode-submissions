class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column_dict={}
        row_dict={}
        sub_dict={}
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] =='.':
                    continue
                if j not in column_dict:
                    column_dict[j]=[]
                if i not in row_dict:
                    row_dict[i]=[]
                st=f'{i//3},{j//3}'
                if st not in sub_dict:
                    sub_dict[st]=[]
                
                if board[i][j] in column_dict[j] or board[i][j] in row_dict[i] or board[i][j] in sub_dict[st]:
                    return False
                
                column_dict[j].append(board[i][j])
                row_dict[i].append(board[i][j])
                sub_dict[st].append(board[i][j])
        return True
