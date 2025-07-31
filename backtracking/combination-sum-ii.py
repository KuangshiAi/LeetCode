class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = set()
        def backtrack(seq, start, total):
            if total > target:
                return
            if total == target:
                res.add(tuple(seq))
            for i in range(start, len(candidates)):
                seq.append(candidates[i])
                backtrack(seq, i+1, total+candidates[i])
                seq.pop()
        backtrack([], 0, 0)
        res = list(res)
        return res