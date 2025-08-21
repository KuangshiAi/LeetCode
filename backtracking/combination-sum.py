class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        def backtrack(seq, total, start):
            if total == target:
                res.append(seq[:])
                return
            if total > target:
                return
            for i in range(start, len(candidates)):
                seq.append(candidates[i])
                backtrack(seq, total+candidates[i], i)
                seq.pop()
        backtrack([], 0, 0)
        return res

        