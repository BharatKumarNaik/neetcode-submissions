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
                    queue.append([i,j])
                    visited.add((i,j))
        
        def bfs(i,j):
            if i not in range(rows) or j not in range(cols):
                return
            if (i,j) in visited:
                return
            if grid[i][j]==-1:
                return
            queue.append([i,j])
            visited.add((i,j))
        
        dist=0
        while queue:
            n=len(queue)
            for k in range(n):
                i,j=queue.pop(0)
                grid[i][j]=dist
                bfs(i+1,j)
                bfs(i-1,j)
                bfs(i,j+1)
                bfs(i,j-1)
            dist+=1
        
