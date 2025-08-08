class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp = [1] * len(nums)
        # for i in range(len(nums)):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             dp[i] = max(dp[i], dp[j]+1)
        # return max(dp)
        tails = []
        # first >= x
        def lower_bound(arr, target):
            left, right = 0, len(arr)
            while left < right:
                mid = (left + right)//2
                if arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left
        for x in nums:
            i = lower_bound(tails, x)
            if i == len(tails):
                tails.append(x)
            else:
                tails[i] = x
        return len(tails)
