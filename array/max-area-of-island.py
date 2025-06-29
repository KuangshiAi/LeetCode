class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.max = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        def dfs(r,c,visited):
            if not (0<=r<rows and 0<=c<cols):
                return 0
            if (r,c) in visited or grid[r][c]==0:
                return 0
            visited.add((r,c))
            return 1+dfs(r+1,c,visited)+dfs(r-1,c,visited)+dfs(r,c+1,visited)+dfs(r,c-1,visited)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    self.max = max(self.max, dfs(i,j,visited))
        return self.max
            