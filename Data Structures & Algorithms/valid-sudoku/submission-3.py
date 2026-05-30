class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # first condition: row wise duplicate check
        for i in range(len(board)):
            for j in range(9-1):
                temp=board[i][:j]+board[i][j+1:]
                # print(board[i][j],temp)
                if board[i][j] !='.' and board[i][j] in temp:
                    return False
        print('cleared first condition')
        # second condition: column wise duplicates check
        for j in range(len(board)):
            temp=[]
            for i in range(len(board[i])):
                # print(board[i][j],temp)
                if board[i][j] !='.' and board[i][j] in temp:
                    return False
                temp.append(board[i][j])
        print('cleared second condtion')
        # Thrid condition: sub matrix duplicates check
        data={}
        for i in range(len(board)):
            for j in range(len(board[i])):
                # print(data)
                st=f'{i//3},{j//3}'
                if st not in data:
                    data[st]=[]
                if board[i][j] !='.' and board[i][j] in data[st]:
                    return False
                data[st].append(board[i][j])
        return True