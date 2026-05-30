class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited=set()
        res=0
        def dfs(i,j):
            if (i not in range(len(grid)) or j not in range(len(grid[0]))):
                return True
            if ((i,j) in visited):
                return False
            if grid[i][j]=="1":
                visited.add((i,j))
                dfs(i+1,j)
                dfs(i-1,j)
                dfs(i,j+1)
                dfs(i,j-1)
            return True
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1" and dfs(i,j):
                    res+=1
        return res
        