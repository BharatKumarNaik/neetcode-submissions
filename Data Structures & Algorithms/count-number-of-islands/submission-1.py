class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res=0
        ROWS=len(grid)
        COLS=len(grid[0])
        self.grid=grid
        def dfs(r,c):
            if r<0 or c<0 or r>=ROWS or c>=COLS or self.grid[r][c]=='0':
                return
            
            self.grid[r][c]='0'
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            return

        
        for r in range(ROWS):
            for c in range(COLS):
                if self.grid[r][c]=='0':
                    continue
                # else found a new island
                dfs(r,c) #dfs will parse the entire island and mark it as 0
                res+=1
        return res