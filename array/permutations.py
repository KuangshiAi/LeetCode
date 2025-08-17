class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def backtrack(path, used):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                else:
                    path.append(nums[i])
                    used[i] = 1
                    backtrack(path, used)
                    path.pop()
                    used[i] = 0
        backtrack([],[0]*len(nums))
        return res