class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def backtrack(subset, start, k):
            if k == 0:
                res.append(subset[:])
                return
            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(subset, i+1, k-1)
                subset.pop()
        for k in range(len(nums)+1):
            backtrack([], 0, k)
        return res