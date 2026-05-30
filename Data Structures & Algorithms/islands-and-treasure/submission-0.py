class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # for shortest path BFS is used
        # key is to go from gate to all other node
        rows,cols=len(grid),len(grid[0])
        visited=set()
        queue=[]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==0:
                    visited.add((i,j))
                    queue.append((i,j))
        # entire queue has all gate location
        def bfs(i,j):
            if i not in range(rows) or j not in range(cols):
                return
            if (i,j) in visited:
                return
            if grid[i][j]==-1:
                return
            visited.add((i,j))
            queue.append((i,j))

        dist=0
        while queue:
            n=len(queue)
            for i in range(n):
                r,c=queue.pop(0)
                grid[r][c]=dist
                bfs(r+1,c)
                bfs(r-1,c)
                bfs(r,c+1)
                bfs(r,c-1)
            dist+=1
        
