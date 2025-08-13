class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        res = [[1]]
        for i in range(numRows-1):
            cur_row = [1] * (len(res[i])+1)
            for j in range(1, len(cur_row)-1):
                cur_row[j] = res[i][j-1] + res[i][j]
            res.append(cur_row)
        return res
        