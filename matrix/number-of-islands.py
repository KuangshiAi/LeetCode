from collections import deque
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        # def bfs(i,j):
        #     queue = deque()
        #     queue.append((i,j))
        #     visited.add((i,j))
        #     while queue:
        #         cur_row, cur_col = queue.popleft()
        #         for dr,dc in directions:
        #             row = cur_row + dr
        #             col = cur_col + dc
        #             if 0<=row<rows and 0<=col<cols and grid[row][col]=="1" and (row,col) not in visited:
        #                 queue.append((row,col))
        #                 visited.add((row,col))
        def dfs(i,j):
            if (i,j) in visited:
                return
            if (i,j) not in visited and grid[i][j]=="1":
                visited.add((i,j))
            for dr,dc in directions:
                row = i + dr
                col = j + dc
                if 0<=row<rows and 0<=col<cols and grid[row][col]=="1" and (row,col) not in visited:
                    dfs(row, col)

        island_num = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visited:
                    island_num += 1
                    dfs(i,j)
        return island_num
        
        