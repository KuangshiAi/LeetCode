class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # dp[i][j]: smallest sum that ends at grid[i][j]
        m = len(grid)
        n = len(grid[0])
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i == 0 and j>0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                elif j == 0 and i>0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]
        return dp[m-1][n-1]