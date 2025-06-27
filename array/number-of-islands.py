from collections import deque
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        island = 0
        visited = set()
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if 0<=r<rows and 0<=c<cols and grid[r][c]=="1" and (r,c) not in visited:
                        q.append((r,c))
                        visited.add((r,c))


        # def dfs(r,c):
        #     directions = [[1,0], [-1,0], [0,1], [0,-1]]
        #     if (r,c) not in visited and grid[r][c] == "1":
        #         visited.add((r,c))
        #     for dr, dc in directions:
        #         r_, c_ = r + dr, c + dc
        #         if 0<=r_<rows and 0<=c_<cols and grid[r_][c_]=="1" and (r_,c_) not in visited:
        #             dfs(r_,c_)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visited:
                    island += 1
                    bfs(i,j)
        return island

        