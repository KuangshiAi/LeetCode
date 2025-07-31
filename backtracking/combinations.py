class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        def backtrack(comb, start, k_left):
            if k_left == 0:
                res.append(comb[:])
                return
            for i in range(start, n+1):
                comb.append(i)
                backtrack(comb, i+1, k_left - 1)
                comb.pop()
        backtrack([], 1, k)
        return res
        