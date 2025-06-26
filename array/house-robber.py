class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        bp = [0]*n
        bp[0] = nums[0]
        bp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            bp[i] = max(bp[i-1], bp[i-2]+nums[i])
        return bp[n-1]
        