class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # window parsing but on higher dimension: 2D
        # left: i,j-=1
        # right: i,j+=1
        # up: i-=1,j
        # down: i+=1,j
        memo=set()

        def dfs(r,c,i):
            if i==len(word):
                return True
            
            if (min(r,c)<0 or r>=len(board) or c>=len(board[0]) or word[i]!=board[r][c] or (r,c) in memo):
                return False
            
            memo.add((r,c))
            down=dfs(r+1,c,i+1)
            up=dfs(r-1,c,i+1)
            left=dfs(r,c-1,i+1)
            right=dfs(r,c+1,i+1)

            res=down or up or left or right
            memo.remove((r,c))
            return res
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r,c,0):
                    return True
        
        return False