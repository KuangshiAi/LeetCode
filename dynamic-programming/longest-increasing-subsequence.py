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
        #             dp[i] = max(dp[j]+1, dp[i])
        # return max(dp)

        tails = [nums[0]]
        for k in range(1, len(nums)):
            i, j =0, len(tails)
            while i<j:
                m = (i+j)//2
                if tails[m] < nums[k]:
                    i = m+1
                else:
                    j = m
            if i == len(tails):
                tails.append(nums[k])
            else:
                tails[i] = nums[k]
            
        return len(tails)
        
        