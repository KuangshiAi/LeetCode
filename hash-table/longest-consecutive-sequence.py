class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        res = 0
        for x in num_set:
            if x-1 not in num_set:
                y=x
                while y in num_set:
                    y += 1
                res = max(res, y-x)

        return res