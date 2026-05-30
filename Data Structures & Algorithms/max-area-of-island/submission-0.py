class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited=set()
        rows,cols=len(grid),len(grid[0])
        max_area=0
        def dfs(i,j,area=0):
            if (i not in range(rows) or j not in range(cols)):
                return 0
            if (i,j) in visited:
                return 0
            visited.add((i,j))
            nonlocal max_area
            if grid[i][j]==1:
                area+=grid[i][j]
            else:
                return 0
            area+=dfs(i+1,j)+dfs(i-1,j)+dfs(i,j+1)+dfs(i,j-1)
            max_area=max(max_area,area)
            return area
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    dfs(i,j,0)
        return max_area

