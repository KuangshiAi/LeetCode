class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        visited = set()
        def dfs(r,c,visited):
            if not (0<=r<rows and 0<=c<cols):
                return 1
            if grid[r][c]==0:
                return 1
            if (r,c) in visited:
                return 0
            visited.add((r,c))
            return dfs(r-1,c,visited) + dfs(r+1,c,visited) + dfs(r,c+1,visited) + dfs(r,c-1,visited)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    return dfs(i,j,visited)
        