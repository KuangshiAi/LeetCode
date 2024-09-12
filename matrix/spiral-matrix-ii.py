class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0]*n for _ in range(n)]
        count = 1
        mid = n // 2
        loop = n // 2
        start_x = 0
        start_y = 0
        for offset in range(1, loop+1):
            for i in range(start_y, n-offset):
                res[start_x][i] = count
                count += 1
            for j in range(start_y, n-offset):
                res[j][n-offset] = count
                count += 1
            for i in range(n-offset, start_y, -1):
                res[n-offset][i] = count
                count += 1
            for j in range(n-offset, start_x, -1):
                res[j][start_y] = count
                count += 1
            start_x += 1
            start_y += 1
        if res[mid][mid] == 0:
            res[mid][mid] = count
        return res
        