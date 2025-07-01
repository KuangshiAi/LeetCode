class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # self.max = nums[0]
        # slow = fast = 0
        # cur_sum = 0
        # for fast in range(len(nums)):
        #     if cur_sum < 0:
        #         slow = fast
        #         cur_sum = nums[slow]
        #     else:
        #         cur_sum += nums[fast]
        #     if cur_sum > self.max:
        #         self.max = cur_sum
        # return self.max

        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if dp[i-1] <= 0:
                dp[i] = nums[i]
            else:
                dp[i] = dp[i-1] + nums[i]
        return max(dp)