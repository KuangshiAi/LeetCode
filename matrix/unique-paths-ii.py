class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        dp = []
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        for i in range(m):
            cur_row = []
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    cur_row.append(0)
                else:
                    cur_row.append(1)
            dp.append(cur_row)
        # further process first row and first col
        for i in range(m):
            if dp[i][0] == 0:
                break
        for k in range(i+1,m):
            dp[k][0] = 0

        for j in range(n):
            if dp[0][j] == 0:
                break
        for k in range(j+1,n):
            dp[0][k] = 0
        for i in range(1, m):
            for j in range(1,n):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                else:
                    dp[i][j] = 0
        return dp[m-1][n-1]
        