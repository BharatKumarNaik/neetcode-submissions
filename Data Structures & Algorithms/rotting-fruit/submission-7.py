class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue=[]
        visited=set()
        fresh=0
        rows,cols=len(grid),len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    visited.add((i,j))
                    queue.append([i,j])
                elif grid[i][j]==1:
                    fresh+=1
        
        def bfs(i,j):
            if i not in range(rows) or j not in range(cols):
                return
            if grid[i][j]==0:
                return
            if (i,j) in visited:
                return
            visited.add((i,j))
            queue.append([i,j])
            nonlocal fresh
            fresh-=1

        time=0
        rot=True
        while queue:
            n=len(queue)
            print(queue)
            for k in range(n):
                l,m=queue.pop(0)
                print(l,m)
                bfs(l+1,m)
                bfs(l-1,m)
                bfs(l,m+1)
                bfs(l,m-1)
            if not rot:
                time+=1
            rot=False
        return time if fresh==0 else -1
