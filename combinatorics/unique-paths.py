class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # dp[i][j]: number of pathes to move to (i,j)
        dp = []
        for i in range(m):
            cur_row = []
            for j in range(n):
                cur_row.append(1)
            dp.append(cur_row)
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
