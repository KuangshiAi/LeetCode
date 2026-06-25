class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        left = 0
        right = len(nums)-1
        res = 0
        while left < right:
            cur = nums[left]+nums[right]
            if cur==k:
                res+=1
                left+=1
                right-=1
            elif cur > k:
                right-=1
            else:
                left+=1
        return res
        