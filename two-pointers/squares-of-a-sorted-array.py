class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            res.append(0)
        i = 0
        j = len(nums) - 1
        k = len(nums) - 1
        while i<= j:
            if nums[i] **2 < nums[j]**2:
                res[k] = nums[j]**2
                j -= 1
            else:
                res[k] = nums[i]**2
                i += 1
            k -= 1
        return res
        