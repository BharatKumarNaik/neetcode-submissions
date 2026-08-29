class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS=len(grid)
        COLS=len(grid[0])
        maxArea=0
        self.grid=grid
        def dfs(r,c):
            if r<0 or c<0 or r>=ROWS or c>=COLS or self.grid[r][c]==0:
                return 0
            self.grid[r][c]=0
            area=dfs(r+1,c)+dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1)+1
            return area
        
        for r in range(ROWS):
            for c in range(COLS):
                if self.grid[r][c]==1:
                    maxArea=max(maxArea,dfs(r,c))
        return maxArea
