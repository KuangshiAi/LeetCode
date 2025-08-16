class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        goal = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] + i >= goal:
                goal = i
        if goal <= 0:
            return True
        else:
            return False