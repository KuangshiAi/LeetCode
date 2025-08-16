class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * len(nums) # dp[i]: the minimal jumps needed from i to the end
        for i in range(len(nums)-2, -1, -1):
            min_jump = float('inf')
            for j in range(i+1, min(i+nums[i]+1, len(nums))):
                min_jump = min(min_jump, dp[j])
            dp[i] = min_jump + 1
        return dp[0]
        