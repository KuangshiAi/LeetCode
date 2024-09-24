class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        buffer = {}
        for i in range(len(nums)):
            if target - nums[i] in buffer.keys():
                return [buffer[target - nums[i]], i]
            else:
                buffer[nums[i]] = i
        