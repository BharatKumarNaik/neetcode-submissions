class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # up: r-1,c
        # down: r+1, c
        # left: r, c-1
        # right: r, c+1
        memo=set()

        # r and c are the location in the board
        # i is the index of the word
        def dfs(r,c,i):
            if i==len(word):
                return True
            
            if min(r,c)<0 or r>=len(board) or c>=len(board[0]):
                return False
            
            if board[r][c]!=word[i] or (r,c) in memo:
                # means either already parsed or char missmatch
                return False
            
            memo.add((r,c))
            up=dfs(r-1,c,i+1)
            down=dfs(r+1,c,i+1)
            left=dfs(r,c-1,i+1)
            right=dfs(r,c+1,i+1)

            res=up or down or left or right
            memo.remove((r,c))
            return res
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                res=dfs(r,c,0)
                if res:
                    return True
        return False
